import { useEffect, useState, useMemo } from 'react'
import { User } from 'lucide-react'
import { useMockExamStore } from '@/stores/mockExamStore'
import { useAppStore } from '@/store/useAppStore'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

function formatTime(ms: number) {
  if (ms <= 0) return '00:00:00'
  const s = Math.floor(ms / 1000)
  const h = Math.floor(s / 3600)
  const m = Math.floor((s % 3600) / 60)
  const sec = s % 60
  return [h, m, sec].map((n) => String(n).padStart(2, '0')).join(':')
}

export function MockExamDashboard() {
  const phase = useMockExamStore((s) => s.phase)

  if (phase === 'setup') return <MockExamSetup />
  if (phase === 'instructions') return <MockExamInstructions />
  if (phase === 'active') return <MockExamActive />
  return <MockExamResults />
}

function MockExamSetup() {
  const config = useMockExamStore((s) => s.config)
  const setConfig = useMockExamStore((s) => s.setConfig)
  const setPhase = useMockExamStore((s) => s.setPhase)
  const setInstructionsAccepted = useMockExamStore((s) => s.setInstructionsAccepted)
  const navRows = useAppStore((s) => s.navRows)
  const loadChapter = useAppStore((s) => s.loadChapter)

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const chapters = useMemo(() => {
    return navRows
      .filter((r) => r.type === 'entry')
      .map((r) => r.type === 'entry' ? r.entry : null)
      .filter(Boolean) as { id: string; title: string }[]
  }, [navRows])

  const handleProceed = async () => {
    setLoading(true)
    setError(null)
    
    try {
      let pool: any[] = []
      
      // Only objective question types — no descriptive answers in a timed exam
      const OBJECTIVE_TYPES = ['mcq', 'true_false', 'assertion_reason']

      // Load selected chapter or all if 'random'
      if (config.source === 'random') {
         const shuffled = [...chapters].sort(() => 0.5 - Math.random()).slice(0, 10)
         for (const ch of shuffled) {
           const data = await loadChapter(ch.id)
           if (data) pool.push(...data.items.filter(i => OBJECTIVE_TYPES.includes(i.type)))
         }
      } else {
         if (!config.chapterId) {
            setError('Please select a chapter.')
            setLoading(false)
            return
         }
         const data = await loadChapter(config.chapterId)
         if (data) {
           pool = data.items.filter(i => OBJECTIVE_TYPES.includes(i.type))
         }
      }
      
      if (pool.length === 0) {
        setError('No questions found for this selection.')
        setLoading(false)
        return
      }
      
      // Shuffle and slice
      const selected = pool.sort(() => 0.5 - Math.random()).slice(0, config.count)
      
      setInstructionsAccepted(false)
      // Transition to instructions, but pre-load items into startTest later
      // Wait, we need to pass items to startTest, but startTest transitions to 'active'.
      // For now, we transition to 'instructions' and we can keep `selected` locally or in a temp store.
      // Actually, since startTest handles items, let's add a setExamItems to store or just transition directly.
      // Let's pass them when we click Start. So we need to store them in the mockExamStore.
      
      // I'll update store to accept pre-loaded items so instructions can see count.
      useMockExamStore.setState({ examItems: selected })
      setPhase('instructions')
    } catch (e) {
      setError('Error loading questions.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="mx-auto max-w-4xl px-4 py-8">
      <div className="flex items-center justify-between mb-6 bg-white p-4 border rounded-lg shadow-sm dark:bg-zinc-900 dark:border-zinc-800">
        <div className="flex items-center gap-4">
          <div className="h-12 w-12 rounded-full bg-blue-800 text-white flex items-center justify-center font-bold text-xs text-center leading-tight">
            NTA<br />Mock
          </div>
          <div>
            <h1 className="font-bold text-blue-900 dark:text-blue-400 text-lg">National Testing Agency — Test Practice Centre</h1>
            <p className="text-sm text-zinc-500">Computer Based Test (CBT) Mock Examination · Harrison's</p>
          </div>
        </div>
      </div>

      <div className="bg-white border rounded-lg p-6 shadow-sm dark:bg-zinc-900 dark:border-zinc-800">
        <h2 className="text-xl font-bold mb-2 border-b pb-2 border-blue-800 dark:border-blue-500">Mock Test Configuration</h2>
        <p className="text-sm text-zinc-600 dark:text-zinc-400 mb-6 mt-2">
          Welcome to the Mock Test Centre. Select your paper below and click Proceed to Instructions.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
          <div>
            <label className="block text-xs font-bold text-zinc-700 dark:text-zinc-300 uppercase mb-1">Question Source</label>
            <select 
              className="w-full border rounded p-2 text-sm bg-white dark:bg-zinc-800 dark:border-zinc-700"
              value={config.source}
              onChange={(e) => setConfig({ source: e.target.value as any })}
            >
              <option value="chapter">Specific Chapter</option>
              <option value="random">Random (across topics)</option>
            </select>
          </div>

          {config.source === 'chapter' && (
            <div>
              <label className="block text-xs font-bold text-zinc-700 dark:text-zinc-300 uppercase mb-1">Chapter</label>
              <select 
                className="w-full border rounded p-2 text-sm bg-white dark:bg-zinc-800 dark:border-zinc-700"
                value={config.chapterId || ''}
                onChange={(e) => setConfig({ chapterId: e.target.value })}
              >
                <option value="">— Select Chapter —</option>
                {chapters.map(ch => (
                  <option key={ch.id} value={ch.id}>{ch.title}</option>
                ))}
              </select>
            </div>
          )}

          <div>
            <label className="block text-xs font-bold text-zinc-700 dark:text-zinc-300 uppercase mb-1">Number of Questions</label>
            <input 
              type="number" min="1" max="200" 
              className="w-full border rounded p-2 text-sm bg-white dark:bg-zinc-800 dark:border-zinc-700"
              value={config.count}
              onChange={(e) => setConfig({ count: parseInt(e.target.value) || 20 })}
            />
          </div>

          <div>
            <label className="block text-xs font-bold text-zinc-700 dark:text-zinc-300 uppercase mb-1">Duration (minutes)</label>
            <input 
              type="number" min="0" max="300" 
              className="w-full border rounded p-2 text-sm bg-white dark:bg-zinc-800 dark:border-zinc-700"
              value={config.durationMin}
              onChange={(e) => setConfig({ durationMin: parseInt(e.target.value) || 0 })}
            />
          </div>
        </div>

        {error && <p className="text-red-600 text-sm mb-4 font-semibold">{error}</p>}

        <div className="flex justify-center mt-6">
          <Button onClick={handleProceed} disabled={loading} className="bg-green-700 hover:bg-green-800 text-white font-bold px-8">
            {loading ? 'Loading...' : 'PROCEED TO INSTRUCTIONS'}
          </Button>
        </div>
      </div>
    </div>
  )
}

function MockExamInstructions() {
  const config = useMockExamStore((s) => s.config)
  const items = useMockExamStore((s) => s.examItems)
  const setPhase = useMockExamStore((s) => s.setPhase)
  const accepted = useMockExamStore((s) => s.instructionsAccepted)
  const setAccepted = useMockExamStore((s) => s.setInstructionsAccepted)
  const startTest = useMockExamStore((s) => s.startTest)

  return (
    <div className="mx-auto max-w-4xl px-4 py-8 flex flex-col h-[calc(100vh-80px)]">
      <div className="bg-white border rounded-t-lg p-4 mb-2 shadow-sm dark:bg-zinc-900 dark:border-zinc-800 shrink-0">
        <h1 className="text-xl font-bold text-blue-900 dark:text-blue-400">General Instructions</h1>
        <p className="text-sm text-zinc-600 dark:text-zinc-400">Mock Test · {items.length} questions · {config.durationMin} min</p>
      </div>

      <div className="bg-white border p-6 overflow-y-auto flex-1 shadow-sm text-sm leading-relaxed dark:bg-zinc-900 dark:border-zinc-800">
        <h2 className="font-bold text-blue-800 dark:text-blue-500 mb-2">Please read the instructions carefully</h2>
        <p className="mb-4"><strong>Total duration</strong> of this mock test is <strong>{config.durationMin} min</strong>.</p>
        <p className="mb-4">The countdown timer in the top right corner of the screen will display the remaining time. When the timer reaches zero, the examination will end by itself.</p>
        
        <h2 className="font-bold text-blue-800 dark:text-blue-500 mb-2 mt-6">Question Palette</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-2 mb-4 bg-zinc-50 p-4 border rounded dark:bg-zinc-800 dark:border-zinc-700">
          <div className="flex items-center gap-2"><div className="w-6 h-6 bg-zinc-400 rounded-sm"></div> Not Visited</div>
          <div className="flex items-center gap-2"><div className="w-6 h-6 bg-orange-600 [clip-path:polygon(15%_0,85%_0,100%_100%,0_100%)]"></div> Not Answered</div>
          <div className="flex items-center gap-2"><div className="w-6 h-6 bg-green-700 [clip-path:polygon(50%_0,100%_38%,82%_100%,18%_100%,0_38%)]"></div> Answered</div>
          <div className="flex items-center gap-2"><div className="w-6 h-6 bg-purple-800 rounded-full"></div> Marked for Review</div>
          <div className="flex items-center gap-2"><div className="w-6 h-6 bg-purple-800 rounded-full relative"><span className="absolute bottom-[-2px] right-[2px] text-[8px] text-green-500 font-bold">✓</span></div> Answered & Marked</div>
        </div>

        <div className="mt-6 bg-yellow-50 border border-yellow-400 p-4 rounded flex gap-3 items-start dark:bg-yellow-900/20 dark:border-yellow-700">
          <input type="checkbox" className="mt-1" checked={accepted} onChange={(e) => setAccepted(e.target.checked)} id="accept-instr" />
          <label htmlFor="accept-instr" className="text-sm font-medium">
            I have read and understood the instructions. I declare that I am ready to begin the CBT Mock Examination.
          </label>
        </div>
      </div>

      <div className="flex justify-between mt-4 shrink-0">
        <Button variant="outline" onClick={() => setPhase('setup')}>← Back</Button>
        <Button disabled={!accepted} onClick={() => startTest(items)} className="bg-blue-600 hover:bg-blue-700 text-white font-bold">Start Mock Test</Button>
      </div>
    </div>
  )
}

function MockExamActive() {
  const store = useMockExamStore()
  const [timeLeft, setTimeLeft] = useState(0)

  useEffect(() => {
    if (!store.endsAt) return
    const interval = setInterval(() => {
      const now = Date.now()
      if (now >= store.endsAt!) {
        store.submitExam()
        clearInterval(interval)
      } else {
        setTimeLeft(store.endsAt! - now)
      }
    }, 1000)
    return () => clearInterval(interval)
  }, [store.endsAt])

  const item = store.examItems[store.index]
  if (!item) return null

  const draft = store.draft[item.id]
  
  const statusCounts = { notVisited: 0, notAnswered: 0, answered: 0, markedReview: 0, answeredMarked: 0 }
  
  store.examItems.forEach((it, i) => {
    const hasAns = store.responses[it.id]?.value !== undefined
    const isMarked = store.marked[it.id]
    const isVisited = store.visited[it.id]
    
    if (isMarked && hasAns) statusCounts.answeredMarked++
    else if (isMarked && !hasAns) statusCounts.markedReview++
    else if (hasAns) statusCounts.answered++
    else if (isVisited || i === store.index) statusCounts.notAnswered++
    else statusCounts.notVisited++
  })

  const getStatusClass = (id: string, idx: number) => {
    const hasAns = store.responses[id]?.value !== undefined
    const isMarked = store.marked[id]
    const isVisited = store.visited[id]
    
    if (isMarked && hasAns) return 'bg-purple-800 rounded-full relative after:content-["✓"] after:absolute after:bottom-[-2px] after:right-[2px] after:text-[10px] after:text-green-500 after:font-bold'
    if (isMarked && !hasAns) return 'bg-purple-800 rounded-full'
    if (hasAns) return 'bg-green-700 [clip-path:polygon(50%_0,100%_38%,82%_100%,18%_100%,0_38%)]'
    if (isVisited || idx === store.index) return 'bg-orange-600 [clip-path:polygon(15%_0,85%_0,100%_100%,0_100%)]'
    return 'bg-zinc-400 rounded-sm'
  }

  return (
    <div className="flex flex-col h-[calc(100vh-48px)] bg-zinc-100 dark:bg-zinc-950 font-sans absolute inset-0 z-50">
      <header className="flex bg-white border-b-2 border-blue-900 shrink-0 dark:bg-zinc-900">
        <div className="flex items-center gap-2 p-2 border-r dark:border-zinc-800">
          <div className="w-10 h-10 bg-blue-900 text-white rounded-full flex items-center justify-center font-bold text-[10px]">NTA</div>
        </div>
        <div className="flex-1 flex items-center p-2 gap-4">
          <div className="w-14 h-16 bg-zinc-200 border flex items-center justify-center dark:bg-zinc-800 dark:border-zinc-700"><User className="text-zinc-400" /></div>
          <div className="text-xs">
            <p><span className="font-bold">Candidate Name:</span> Student</p>
            <p><span className="font-bold">Exam Name:</span> MOCK TEST</p>
          </div>
        </div>
        <div className="p-2 border-l bg-zinc-50 flex flex-col justify-center items-center min-w-[120px] dark:bg-zinc-800 dark:border-zinc-700">
          <span className="text-[10px] font-bold text-zinc-500 uppercase">Remaining Time</span>
          <span className="text-xl font-bold text-red-600 tabular-nums">{store.endsAt ? formatTime(timeLeft) : '--:--:--'}</span>
        </div>
      </header>

      <div className="flex flex-1 min-h-0 relative">
        <div className="flex-1 flex flex-col min-w-0 bg-white m-2 border dark:bg-zinc-900 dark:border-zinc-800">
          <div className="flex-1 overflow-y-auto p-4">
            <div className="font-bold border-b pb-2 mb-4">Question {store.index + 1}:</div>
            
            <div className="prose dark:prose-invert max-w-none text-sm mb-6">
              {item.type === 'mcq' && ((item as any).stem || (item as any).question)}
              {item.type === 'true_false' && (item as any).statement}
              {item.type === 'assertion_reason' && (
                <div>
                  <p><strong>Assertion (A):</strong> {(item as any).assertion}</p>
                  <p className="mt-2"><strong>Reason (R):</strong> {(item as any).reason}</p>
                </div>
              )}
              {['shortanswer', 'why', 'how'].includes(item.type) && ((item as any).question || (item as any).stem)}
            </div>

            <div className="space-y-3">
              {item.type === 'mcq' && (item as any).options?.map((opt: string, i: number) => (
                <label key={i} className={cn("flex items-center gap-3 p-2 border rounded cursor-pointer hover:bg-zinc-50 dark:hover:bg-zinc-800", draft === i && "bg-blue-50 border-blue-300 dark:bg-blue-900/30")}>
                  <input type="radio" name="opt" checked={draft === i} onChange={() => store.setDraft(item.id, i)} className="w-4 h-4 text-blue-600" />
                  <span>{opt}</span>
                </label>
              ))}
              
              {item.type === 'true_false' && ['True', 'False'].map((opt) => (
                <label key={opt} className={cn("flex items-center gap-3 p-2 border rounded cursor-pointer hover:bg-zinc-50 dark:hover:bg-zinc-800", String(draft) === String(opt === 'True') && "bg-blue-50 border-blue-300 dark:bg-blue-900/30")}>
                  <input type="radio" name="tf" checked={String(draft) === String(opt === 'True')} onChange={() => store.setDraft(item.id, opt === 'True')} className="w-4 h-4 text-blue-600" />
                  <span>{opt}</span>
                </label>
              ))}

              {item.type === 'assertion_reason' && ['Both A and R are true and R is the correct explanation of A', 'Both A and R are true but R is not the correct explanation of A', 'A is true but R is false', 'A is false but R is true'].map((opt, i) => (
                <label key={i} className={cn("flex items-center gap-3 p-2 border rounded cursor-pointer hover:bg-zinc-50 dark:hover:bg-zinc-800", draft === i && "bg-blue-50 border-blue-300 dark:bg-blue-900/30")}>
                  <input type="radio" name="ar" checked={draft === i} onChange={() => store.setDraft(item.id, i)} className="w-4 h-4 text-blue-600" />
                  <span>{opt}</span>
                </label>
              ))}

              {['shortanswer', 'why', 'how', 'fill_blank'].includes(item.type) && (
                <textarea 
                  className="w-full border rounded p-3 text-sm min-h-[100px] dark:bg-zinc-800 dark:border-zinc-700" 
                  placeholder="Type your answer here..."
                  value={draft || ''}
                  onChange={(e) => store.setDraft(item.id, e.target.value)}
                />
              )}
            </div>
          </div>

          <div className="flex flex-wrap gap-2 p-3 bg-zinc-50 border-t shrink-0 dark:bg-zinc-800 dark:border-zinc-700">
            <button onClick={() => store.saveAndNext()} className="px-3 py-2 text-xs font-bold text-white bg-green-700 border border-green-900 rounded uppercase">Save & Next</button>
            <button onClick={() => store.clearResponse(item.id)} className="px-3 py-2 text-xs font-bold bg-white border border-zinc-400 rounded uppercase dark:bg-zinc-700 dark:text-zinc-200">Clear</button>
            <button onClick={() => store.saveAndMarkReview()} className="px-3 py-2 text-xs font-bold text-white bg-orange-600 border border-orange-800 rounded uppercase">Save & Mark for Review</button>
            <button onClick={() => store.markReviewAndNext()} className="px-3 py-2 text-xs font-bold text-white bg-blue-700 border border-blue-900 rounded uppercase">Mark for Review & Next</button>
          </div>
          
          <div className="flex justify-between items-center p-3 border-t shrink-0 dark:border-zinc-700">
            <div className="flex gap-2">
              <button onClick={() => store.goToIndex(store.index - 1, false)} disabled={store.index <= 0} className="px-4 py-2 text-xs bg-white border rounded disabled:opacity-50 dark:bg-zinc-800">{'<< Back'}</button>
              <button onClick={() => store.goToIndex(store.index + 1, false)} disabled={store.index >= store.examItems.length - 1} className="px-4 py-2 text-xs bg-white border rounded disabled:opacity-50 dark:bg-zinc-800">{'Next >>'}</button>
            </div>
            <button onClick={() => { if(confirm('Submit mock test?')) store.submitExam() }} className="px-6 py-2 text-sm font-bold text-white bg-green-700 rounded">Submit</button>
          </div>
        </div>

        <aside className={cn("w-[280px] bg-white my-2 mr-2 border flex flex-col transition-all overflow-hidden dark:bg-zinc-900 dark:border-zinc-800", store.paletteHidden && "w-0 border-0 mr-0")}>
          <div className="p-2 border-b text-[10px] shrink-0 dark:border-zinc-700">
            <h4 className="font-bold mb-2">Question Palette</h4>
            <div className="grid grid-cols-2 gap-1">
              <div className="flex items-center gap-1"><div className="w-4 h-4 bg-zinc-400 rounded-sm"></div> <span className="font-bold ml-auto">{statusCounts.notVisited}</span> Not Visited</div>
              <div className="flex items-center gap-1"><div className="w-4 h-4 bg-orange-600 [clip-path:polygon(15%_0,85%_0,100%_100%,0_100%)]"></div> <span className="font-bold ml-auto">{statusCounts.notAnswered}</span> Not Answered</div>
              <div className="flex items-center gap-1"><div className="w-4 h-4 bg-green-700 [clip-path:polygon(50%_0,100%_38%,82%_100%,18%_100%,0_38%)]"></div> <span className="font-bold ml-auto">{statusCounts.answered}</span> Answered</div>
              <div className="flex items-center gap-1"><div className="w-4 h-4 bg-purple-800 rounded-full"></div> <span className="font-bold ml-auto">{statusCounts.markedReview}</span> Marked Review</div>
              <div className="flex items-center gap-1 col-span-2"><div className="w-4 h-4 bg-purple-800 rounded-full relative"><span className="absolute bottom-[-2px] right-[1px] text-[6px] text-green-500 font-bold">✓</span></div> <span className="font-bold ml-auto">{statusCounts.answeredMarked}</span> Answered & Marked</div>
            </div>
          </div>
          <div className="flex-1 overflow-y-auto p-2">
            <div className="grid grid-cols-5 gap-1 content-start">
              {store.examItems.map((it, i) => {
                const isActive = i === store.index
                return (
                  <button
                    key={it.id}
                    onClick={() => store.goToIndex(i, false)}
                    className={cn(
                      "w-full aspect-square flex items-center justify-center text-white text-[10px] font-bold",
                      getStatusClass(it.id, i),
                      isActive && "outline outline-2 outline-blue-500 z-10 scale-110"
                    )}
                  >
                    {i + 1}
                  </button>
                )
              })}
            </div>
          </div>
        </aside>
        
        <button onClick={store.togglePalette} className="absolute right-0 top-1/2 -translate-y-1/2 w-5 h-12 bg-zinc-800 text-white flex items-center justify-center text-xs z-10 opacity-50 hover:opacity-100">
          {store.paletteHidden ? '<' : '>'}
        </button>
      </div>
    </div>
  )
}

function MockExamResults() {
  const store = useMockExamStore()
  const r = store.results!

  return (
    <div className="mx-auto max-w-2xl px-4 py-12">
      <div className="bg-white border rounded-lg p-8 text-center shadow-sm dark:bg-zinc-900 dark:border-zinc-800">
        <h1 className="text-2xl font-bold text-blue-900 mb-2 dark:text-blue-400">Mock Test Complete</h1>
        <div className="text-5xl font-extrabold text-green-700 my-6">{r.correct} / {r.total}</div>
        <p className="text-lg text-zinc-600 mb-8 dark:text-zinc-400">Correct answers · {r.accuracy}% accuracy on attempted</p>
        
        <div className="grid grid-cols-4 gap-4 mb-8">
          <div className="bg-zinc-50 p-4 border rounded dark:bg-zinc-800 dark:border-zinc-700">
            <div className="text-2xl font-bold">{r.total}</div>
            <div className="text-[10px] uppercase text-zinc-500 mt-1">Total</div>
          </div>
          <div className="bg-zinc-50 p-4 border rounded dark:bg-zinc-800 dark:border-zinc-700">
            <div className="text-2xl font-bold">{r.attempted}</div>
            <div className="text-[10px] uppercase text-zinc-500 mt-1">Attempted</div>
          </div>
          <div className="bg-zinc-50 p-4 border rounded dark:bg-zinc-800 dark:border-zinc-700">
            <div className="text-2xl font-bold">{r.correct}</div>
            <div className="text-[10px] uppercase text-zinc-500 mt-1">Correct</div>
          </div>
          <div className="bg-zinc-50 p-4 border rounded dark:bg-zinc-800 dark:border-zinc-700">
            <div className="text-2xl font-bold">{r.total - r.attempted}</div>
            <div className="text-[10px] uppercase text-zinc-500 mt-1">Unanswered</div>
          </div>
        </div>

        <div className="flex justify-center gap-4">
          <Button variant="outline" onClick={() => store.setPhase('setup')}>New Mock Test</Button>
          <Button onClick={() => store.quitTest()} className="bg-blue-600 text-white">Back to Dashboard</Button>
        </div>
      </div>
    </div>
  )
}
