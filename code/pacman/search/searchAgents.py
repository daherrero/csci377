<html>
  <head><script src="//archive.org/includes/analytics.js?v=cf34f82" type="text/javascript"></script>
<script type="text/javascript">window.addEventListener('DOMContentLoaded',function(){var v=archive_analytics.values;v.service='wb';v.server_name='wwwb-app22.us.archive.org';v.server_ms=754;archive_analytics.send_pageview({});});</script><script type="text/javascript" src="/static/js/wbhack.js?v=1527197507.0" charset="utf-8"></script>

<script type="text/javascript">
__wbhack.init('https://web.archive.org/web');
</script>
<link rel="stylesheet" type="text/css" href="/static/css/banner-styles.css?v=1527197507.0" />
<link rel="stylesheet" type="text/css" href="/static/css/iconochive.css?v=1527197507.0" />

<!-- End Wayback Rewrite JS Include -->
  <title>searchAgents.py</title>
  </head>
  <body>
  <h3>searchAgents.py (<a href="http://ai.berkeley.edu/projects/release/search/v1/001/search.zip">original</a>)</h3>
  <hr>
  <pre>
<span style="color: green; font-style: italic"># searchAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


</span><span style="color: darkred">"""
This file contains all of the agents that can be selected to control Pacman.  To
select an agent, use the '-p' option when running pacman.py.  Arguments can be
passed to your agent using '-a'.  For example, to load a SearchAgent that uses
depth first search (dfs), run the following command:

&gt; python pacman.py -p SearchAgent -a fn=depthFirstSearch

Commands to invoke other search strategies can be found in the project
description.

Please only change the parts of the file you are asked to.  Look for the lines
that say

"*** YOUR CODE HERE ***"

The parts you fill in start about 3/4 of the way down.  Follow the project
description for details.

Good luck and happy searching!
"""

</span><span style="color: blue; font-weight: bold">from </span>game <span style="color: blue; font-weight: bold">import </span>Directions
<span style="color: blue; font-weight: bold">from </span>game <span style="color: blue; font-weight: bold">import </span>Agent
<span style="color: blue; font-weight: bold">from </span>game <span style="color: blue; font-weight: bold">import </span>Actions
<span style="color: blue; font-weight: bold">import </span>util
<span style="color: blue; font-weight: bold">import </span>time
<span style="color: blue; font-weight: bold">import </span>search

<span style="color: blue; font-weight: bold">class </span>GoWestAgent<span style="font-weight: bold">(</span>Agent<span style="font-weight: bold">):
    </span><span style="color: red">"An agent that goes West until it can't."

    </span><span style="color: blue; font-weight: bold">def </span>getAction<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: red">"The agent receives a GameState (defined in pacman.py)."
        </span><span style="color: blue; font-weight: bold">if </span>Directions<span style="font-weight: bold">.</span>WEST <span style="color: blue; font-weight: bold">in </span>state<span style="font-weight: bold">.</span>getLegalPacmanActions<span style="font-weight: bold">():
            </span><span style="color: blue; font-weight: bold">return </span>Directions<span style="font-weight: bold">.</span>WEST
        <span style="color: blue; font-weight: bold">else</span><span style="font-weight: bold">:
            </span><span style="color: blue; font-weight: bold">return </span>Directions<span style="font-weight: bold">.</span>STOP

<span style="color: green; font-style: italic">#######################################################
# This portion is written for you, but will only work #
#       after you fill in parts of search.py          #
#######################################################

</span><span style="color: blue; font-weight: bold">class </span>SearchAgent<span style="font-weight: bold">(</span>Agent<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    This very general search agent finds a path using a supplied search
    algorithm for a supplied search problem, then returns actions to follow that
    path.

    As a default, this agent runs DFS on a PositionSearchProblem to find
    location (1,1)

    Options for fn include:
      depthFirstSearch or dfs
      breadthFirstSearch or bfs


    Note: You should NOT change any code in SearchAgent
    """

    </span><span style="color: blue; font-weight: bold">def </span>__init__<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>fn<span style="font-weight: bold">=</span><span style="color: red">'depthFirstSearch'</span><span style="font-weight: bold">, </span>prob<span style="font-weight: bold">=</span><span style="color: red">'PositionSearchProblem'</span><span style="font-weight: bold">, </span>heuristic<span style="font-weight: bold">=</span><span style="color: red">'nullHeuristic'</span><span style="font-weight: bold">):
        </span><span style="color: green; font-style: italic"># Warning: some advanced Python magic is employed below to find the right functions and problems

        # Get the search function from the name and heuristic
        </span><span style="color: blue; font-weight: bold">if </span>fn <span style="color: blue; font-weight: bold">not in </span>dir<span style="font-weight: bold">(</span>search<span style="font-weight: bold">):
            </span><span style="color: blue; font-weight: bold">raise </span>AttributeError<span style="font-weight: bold">, </span>fn <span style="font-weight: bold">+ </span><span style="color: red">' is not a search function in search.py.'
        </span>func <span style="font-weight: bold">= </span>getattr<span style="font-weight: bold">(</span>search<span style="font-weight: bold">, </span>fn<span style="font-weight: bold">)
        </span><span style="color: blue; font-weight: bold">if </span><span style="color: red">'heuristic' </span><span style="color: blue; font-weight: bold">not in </span>func<span style="font-weight: bold">.</span>func_code<span style="font-weight: bold">.</span>co_varnames<span style="font-weight: bold">:
            </span><span style="color: blue; font-weight: bold">print</span><span style="font-weight: bold">(</span><span style="color: red">'[SearchAgent] using function ' </span><span style="font-weight: bold">+ </span>fn<span style="font-weight: bold">)
            </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchFunction <span style="font-weight: bold">= </span>func
        <span style="color: blue; font-weight: bold">else</span><span style="font-weight: bold">:
            </span><span style="color: blue; font-weight: bold">if </span>heuristic <span style="color: blue; font-weight: bold">in </span>globals<span style="font-weight: bold">().</span>keys<span style="font-weight: bold">():
                </span>heur <span style="font-weight: bold">= </span>globals<span style="font-weight: bold">()[</span>heuristic<span style="font-weight: bold">]
            </span><span style="color: blue; font-weight: bold">elif </span>heuristic <span style="color: blue; font-weight: bold">in </span>dir<span style="font-weight: bold">(</span>search<span style="font-weight: bold">):
                </span>heur <span style="font-weight: bold">= </span>getattr<span style="font-weight: bold">(</span>search<span style="font-weight: bold">, </span>heuristic<span style="font-weight: bold">)
            </span><span style="color: blue; font-weight: bold">else</span><span style="font-weight: bold">:
                </span><span style="color: blue; font-weight: bold">raise </span>AttributeError<span style="font-weight: bold">, </span>heuristic <span style="font-weight: bold">+ </span><span style="color: red">' is not a function in searchAgents.py or search.py.'
            </span><span style="color: blue; font-weight: bold">print</span><span style="font-weight: bold">(</span><span style="color: red">'[SearchAgent] using function %s and heuristic %s' </span><span style="font-weight: bold">% (</span>fn<span style="font-weight: bold">, </span>heuristic<span style="font-weight: bold">))
            </span><span style="color: green; font-style: italic"># Note: this bit of Python trickery combines the search algorithm and the heuristic
            </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchFunction <span style="font-weight: bold">= </span><span style="color: blue; font-weight: bold">lambda </span>x<span style="font-weight: bold">: </span>func<span style="font-weight: bold">(</span>x<span style="font-weight: bold">, </span>heuristic<span style="font-weight: bold">=</span>heur<span style="font-weight: bold">)

        </span><span style="color: green; font-style: italic"># Get the search problem type from the name
        </span><span style="color: blue; font-weight: bold">if </span>prob <span style="color: blue; font-weight: bold">not in </span>globals<span style="font-weight: bold">().</span>keys<span style="font-weight: bold">() </span><span style="color: blue; font-weight: bold">or not </span>prob<span style="font-weight: bold">.</span>endswith<span style="font-weight: bold">(</span><span style="color: red">'Problem'</span><span style="font-weight: bold">):
            </span><span style="color: blue; font-weight: bold">raise </span>AttributeError<span style="font-weight: bold">, </span>prob <span style="font-weight: bold">+ </span><span style="color: red">' is not a search problem type in SearchAgents.py.'
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchType <span style="font-weight: bold">= </span>globals<span style="font-weight: bold">()[</span>prob<span style="font-weight: bold">]
        </span><span style="color: blue; font-weight: bold">print</span><span style="font-weight: bold">(</span><span style="color: red">'[SearchAgent] using problem type ' </span><span style="font-weight: bold">+ </span>prob<span style="font-weight: bold">)

    </span><span style="color: blue; font-weight: bold">def </span>registerInitialState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        This is the first time that the agent sees the layout of the game
        board. Here, we choose a path to the goal. In this phase, the agent
        should compute the path to the goal and store it in a local variable.
        All of the work is done in this method!

        state: a GameState object (pacman.py)
        """
        </span><span style="color: blue; font-weight: bold">if </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchFunction <span style="font-weight: bold">== </span><span style="color: blue">None</span><span style="font-weight: bold">: </span><span style="color: blue; font-weight: bold">raise </span>Exception<span style="font-weight: bold">, </span><span style="color: red">"No search function provided for SearchAgent"
        </span>starttime <span style="font-weight: bold">= </span>time<span style="font-weight: bold">.</span>time<span style="font-weight: bold">()
        </span>problem <span style="font-weight: bold">= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchType<span style="font-weight: bold">(</span>state<span style="font-weight: bold">) </span><span style="color: green; font-style: italic"># Makes a new search problem
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actions  <span style="font-weight: bold">= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchFunction<span style="font-weight: bold">(</span>problem<span style="font-weight: bold">) </span><span style="color: green; font-style: italic"># Find a path
        </span>totalCost <span style="font-weight: bold">= </span>problem<span style="font-weight: bold">.</span>getCostOfActions<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actions<span style="font-weight: bold">)
        </span><span style="color: blue; font-weight: bold">print</span><span style="font-weight: bold">(</span><span style="color: red">'Path found with total cost of %d in %.1f seconds' </span><span style="font-weight: bold">% (</span>totalCost<span style="font-weight: bold">, </span>time<span style="font-weight: bold">.</span>time<span style="font-weight: bold">() - </span>starttime<span style="font-weight: bold">))
        </span><span style="color: blue; font-weight: bold">if </span><span style="color: red">'_expanded' </span><span style="color: blue; font-weight: bold">in </span>dir<span style="font-weight: bold">(</span>problem<span style="font-weight: bold">): </span><span style="color: blue; font-weight: bold">print</span><span style="font-weight: bold">(</span><span style="color: red">'Search nodes expanded: %d' </span><span style="font-weight: bold">% </span>problem<span style="font-weight: bold">.</span>_expanded<span style="font-weight: bold">)

    </span><span style="color: blue; font-weight: bold">def </span>getAction<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Returns the next action in the path chosen earlier (in
        registerInitialState).  Return Directions.STOP if there is no further
        action to take.

        state: a GameState object (pacman.py)
        """
        </span><span style="color: blue; font-weight: bold">if </span><span style="color: red">'actionIndex' </span><span style="color: blue; font-weight: bold">not in </span>dir<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">): </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actionIndex <span style="font-weight: bold">= </span><span style="color: red">0
        </span>i <span style="font-weight: bold">= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actionIndex
        <span style="color: blue">self</span><span style="font-weight: bold">.</span>actionIndex <span style="font-weight: bold">+= </span><span style="color: red">1
        </span><span style="color: blue; font-weight: bold">if </span>i <span style="font-weight: bold">&lt; </span>len<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actions<span style="font-weight: bold">):
            </span><span style="color: blue; font-weight: bold">return </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actions<span style="font-weight: bold">[</span>i<span style="font-weight: bold">]
        </span><span style="color: blue; font-weight: bold">else</span><span style="font-weight: bold">:
            </span><span style="color: blue; font-weight: bold">return </span>Directions<span style="font-weight: bold">.</span>STOP

<span style="color: blue; font-weight: bold">class </span>PositionSearchProblem<span style="font-weight: bold">(</span>search<span style="font-weight: bold">.</span>SearchProblem<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    A search problem defines the state space, start state, goal test, successor
    function and cost function.  This search problem can be used to find paths
    to a particular point on the pacman board.

    The state space consists of (x,y) positions in a pacman game.

    Note: this search problem is fully specified; you should NOT change it.
    """

    </span><span style="color: blue; font-weight: bold">def </span>__init__<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>gameState<span style="font-weight: bold">, </span>costFn <span style="font-weight: bold">= </span><span style="color: blue; font-weight: bold">lambda </span>x<span style="font-weight: bold">: </span><span style="color: red">1</span><span style="font-weight: bold">, </span>goal<span style="font-weight: bold">=(</span><span style="color: red">1</span><span style="font-weight: bold">,</span><span style="color: red">1</span><span style="font-weight: bold">), </span>start<span style="font-weight: bold">=</span><span style="color: blue">None</span><span style="font-weight: bold">, </span>warn<span style="font-weight: bold">=</span><span style="color: blue; font-weight: bold">True</span><span style="font-weight: bold">, </span>visualize<span style="font-weight: bold">=</span><span style="color: blue; font-weight: bold">True</span><span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Stores the start and goal.

        gameState: A GameState object (pacman.py)
        costFn: A function from a search state (tuple) to a non-negative number
        goal: A position in the gameState
        """
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls <span style="font-weight: bold">= </span>gameState<span style="font-weight: bold">.</span>getWalls<span style="font-weight: bold">()
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>startState <span style="font-weight: bold">= </span>gameState<span style="font-weight: bold">.</span>getPacmanPosition<span style="font-weight: bold">()
        </span><span style="color: blue; font-weight: bold">if </span>start <span style="font-weight: bold">!= </span><span style="color: blue">None</span><span style="font-weight: bold">: </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>startState <span style="font-weight: bold">= </span>start
        <span style="color: blue">self</span><span style="font-weight: bold">.</span>goal <span style="font-weight: bold">= </span>goal
        <span style="color: blue">self</span><span style="font-weight: bold">.</span>costFn <span style="font-weight: bold">= </span>costFn
        <span style="color: blue">self</span><span style="font-weight: bold">.</span>visualize <span style="font-weight: bold">= </span>visualize
        <span style="color: blue; font-weight: bold">if </span>warn <span style="color: blue; font-weight: bold">and </span><span style="font-weight: bold">(</span>gameState<span style="font-weight: bold">.</span>getNumFood<span style="font-weight: bold">() != </span><span style="color: red">1 </span><span style="color: blue; font-weight: bold">or not </span>gameState<span style="font-weight: bold">.</span>hasFood<span style="font-weight: bold">(*</span>goal<span style="font-weight: bold">)):
            </span><span style="color: blue; font-weight: bold">print </span><span style="color: red">'Warning: this does not look like a regular search maze'

        </span><span style="color: green; font-style: italic"># For display purposes
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_visited<span style="font-weight: bold">, </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_visitedlist<span style="font-weight: bold">, </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_expanded <span style="font-weight: bold">= {}, [], </span><span style="color: red">0 </span><span style="color: green; font-style: italic"># DO NOT CHANGE

    </span><span style="color: blue; font-weight: bold">def </span>getStartState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">):
        </span><span style="color: blue; font-weight: bold">return </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>startState

    <span style="color: blue; font-weight: bold">def </span>isGoalState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span>isGoal <span style="font-weight: bold">= </span>state <span style="font-weight: bold">== </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>goal

        <span style="color: green; font-style: italic"># For display purposes only
        </span><span style="color: blue; font-weight: bold">if </span>isGoal <span style="color: blue; font-weight: bold">and </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>visualize<span style="font-weight: bold">:
            </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_visitedlist<span style="font-weight: bold">.</span>append<span style="font-weight: bold">(</span>state<span style="font-weight: bold">)
            </span><span style="color: blue; font-weight: bold">import </span>__main__
            <span style="color: blue; font-weight: bold">if </span><span style="color: red">'_display' </span><span style="color: blue; font-weight: bold">in </span>dir<span style="font-weight: bold">(</span>__main__<span style="font-weight: bold">):
                </span><span style="color: blue; font-weight: bold">if </span><span style="color: red">'drawExpandedCells' </span><span style="color: blue; font-weight: bold">in </span>dir<span style="font-weight: bold">(</span>__main__<span style="font-weight: bold">.</span>_display<span style="font-weight: bold">): </span><span style="color: green; font-style: italic">#@UndefinedVariable
                    </span>__main__<span style="font-weight: bold">.</span>_display<span style="font-weight: bold">.</span>drawExpandedCells<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_visitedlist<span style="font-weight: bold">) </span><span style="color: green; font-style: italic">#@UndefinedVariable

        </span><span style="color: blue; font-weight: bold">return </span>isGoal

    <span style="color: blue; font-weight: bold">def </span>getSuccessors<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """

        </span>successors <span style="font-weight: bold">= []
        </span><span style="color: blue; font-weight: bold">for </span>action <span style="color: blue; font-weight: bold">in </span><span style="font-weight: bold">[</span>Directions<span style="font-weight: bold">.</span>NORTH<span style="font-weight: bold">, </span>Directions<span style="font-weight: bold">.</span>SOUTH<span style="font-weight: bold">, </span>Directions<span style="font-weight: bold">.</span>EAST<span style="font-weight: bold">, </span>Directions<span style="font-weight: bold">.</span>WEST<span style="font-weight: bold">]:
            </span>x<span style="font-weight: bold">,</span>y <span style="font-weight: bold">= </span>state
            dx<span style="font-weight: bold">, </span>dy <span style="font-weight: bold">= </span>Actions<span style="font-weight: bold">.</span>directionToVector<span style="font-weight: bold">(</span>action<span style="font-weight: bold">)
            </span>nextx<span style="font-weight: bold">, </span>nexty <span style="font-weight: bold">= </span>int<span style="font-weight: bold">(</span>x <span style="font-weight: bold">+ </span>dx<span style="font-weight: bold">), </span>int<span style="font-weight: bold">(</span>y <span style="font-weight: bold">+ </span>dy<span style="font-weight: bold">)
            </span><span style="color: blue; font-weight: bold">if not </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls<span style="font-weight: bold">[</span>nextx<span style="font-weight: bold">][</span>nexty<span style="font-weight: bold">]:
                </span>nextState <span style="font-weight: bold">= (</span>nextx<span style="font-weight: bold">, </span>nexty<span style="font-weight: bold">)
                </span>cost <span style="font-weight: bold">= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>costFn<span style="font-weight: bold">(</span>nextState<span style="font-weight: bold">)
                </span>successors<span style="font-weight: bold">.</span>append<span style="font-weight: bold">( ( </span>nextState<span style="font-weight: bold">, </span>action<span style="font-weight: bold">, </span>cost<span style="font-weight: bold">) )

        </span><span style="color: green; font-style: italic"># Bookkeeping for display purposes
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_expanded <span style="font-weight: bold">+= </span><span style="color: red">1 </span><span style="color: green; font-style: italic"># DO NOT CHANGE
        </span><span style="color: blue; font-weight: bold">if </span>state <span style="color: blue; font-weight: bold">not in </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_visited<span style="font-weight: bold">:
            </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_visited<span style="font-weight: bold">[</span>state<span style="font-weight: bold">] = </span><span style="color: blue; font-weight: bold">True
            </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_visitedlist<span style="font-weight: bold">.</span>append<span style="font-weight: bold">(</span>state<span style="font-weight: bold">)

        </span><span style="color: blue; font-weight: bold">return </span>successors

    <span style="color: blue; font-weight: bold">def </span>getCostOfActions<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>actions<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Returns the cost of a particular sequence of actions. If those actions
        include an illegal move, return 999999.
        """
        </span><span style="color: blue; font-weight: bold">if </span>actions <span style="font-weight: bold">== </span><span style="color: blue">None</span><span style="font-weight: bold">: </span><span style="color: blue; font-weight: bold">return </span><span style="color: red">999999
        </span>x<span style="font-weight: bold">,</span>y<span style="font-weight: bold">= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>getStartState<span style="font-weight: bold">()
        </span>cost <span style="font-weight: bold">= </span><span style="color: red">0
        </span><span style="color: blue; font-weight: bold">for </span>action <span style="color: blue; font-weight: bold">in </span>actions<span style="font-weight: bold">:
            </span><span style="color: green; font-style: italic"># Check figure out the next state and see whether its' legal
            </span>dx<span style="font-weight: bold">, </span>dy <span style="font-weight: bold">= </span>Actions<span style="font-weight: bold">.</span>directionToVector<span style="font-weight: bold">(</span>action<span style="font-weight: bold">)
            </span>x<span style="font-weight: bold">, </span>y <span style="font-weight: bold">= </span>int<span style="font-weight: bold">(</span>x <span style="font-weight: bold">+ </span>dx<span style="font-weight: bold">), </span>int<span style="font-weight: bold">(</span>y <span style="font-weight: bold">+ </span>dy<span style="font-weight: bold">)
            </span><span style="color: blue; font-weight: bold">if </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls<span style="font-weight: bold">[</span>x<span style="font-weight: bold">][</span>y<span style="font-weight: bold">]: </span><span style="color: blue; font-weight: bold">return </span><span style="color: red">999999
            </span>cost <span style="font-weight: bold">+= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>costFn<span style="font-weight: bold">((</span>x<span style="font-weight: bold">,</span>y<span style="font-weight: bold">))
        </span><span style="color: blue; font-weight: bold">return </span>cost

<span style="color: blue; font-weight: bold">class </span>StayEastSearchAgent<span style="font-weight: bold">(</span>SearchAgent<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    An agent for position search with a cost function that penalizes being in
    positions on the West side of the board.

    The cost function for stepping into a position (x,y) is 1/2^x.
    """
    </span><span style="color: blue; font-weight: bold">def </span>__init__<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">):
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchFunction <span style="font-weight: bold">= </span>search<span style="font-weight: bold">.</span>uniformCostSearch
        costFn <span style="font-weight: bold">= </span><span style="color: blue; font-weight: bold">lambda </span>pos<span style="font-weight: bold">: .</span><span style="color: red">5 </span><span style="font-weight: bold">** </span>pos<span style="font-weight: bold">[</span><span style="color: red">0</span><span style="font-weight: bold">]
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchType <span style="font-weight: bold">= </span><span style="color: blue; font-weight: bold">lambda </span>state<span style="font-weight: bold">: </span>PositionSearchProblem<span style="font-weight: bold">(</span>state<span style="font-weight: bold">, </span>costFn<span style="font-weight: bold">, (</span><span style="color: red">1</span><span style="font-weight: bold">, </span><span style="color: red">1</span><span style="font-weight: bold">), </span><span style="color: blue">None</span><span style="font-weight: bold">, </span><span style="color: blue; font-weight: bold">False</span><span style="font-weight: bold">)

</span><span style="color: blue; font-weight: bold">class </span>StayWestSearchAgent<span style="font-weight: bold">(</span>SearchAgent<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    An agent for position search with a cost function that penalizes being in
    positions on the East side of the board.

    The cost function for stepping into a position (x,y) is 2^x.
    """
    </span><span style="color: blue; font-weight: bold">def </span>__init__<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">):
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchFunction <span style="font-weight: bold">= </span>search<span style="font-weight: bold">.</span>uniformCostSearch
        costFn <span style="font-weight: bold">= </span><span style="color: blue; font-weight: bold">lambda </span>pos<span style="font-weight: bold">: </span><span style="color: red">2 </span><span style="font-weight: bold">** </span>pos<span style="font-weight: bold">[</span><span style="color: red">0</span><span style="font-weight: bold">]
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchType <span style="font-weight: bold">= </span><span style="color: blue; font-weight: bold">lambda </span>state<span style="font-weight: bold">: </span>PositionSearchProblem<span style="font-weight: bold">(</span>state<span style="font-weight: bold">, </span>costFn<span style="font-weight: bold">)

</span><span style="color: blue; font-weight: bold">def </span>manhattanHeuristic<span style="font-weight: bold">(</span>position<span style="font-weight: bold">, </span>problem<span style="font-weight: bold">, </span>info<span style="font-weight: bold">={}):
    </span><span style="color: red">"The Manhattan distance heuristic for a PositionSearchProblem"
    </span>xy1 <span style="font-weight: bold">= </span>position
    xy2 <span style="font-weight: bold">= </span>problem<span style="font-weight: bold">.</span>goal
    <span style="color: blue; font-weight: bold">return </span>abs<span style="font-weight: bold">(</span>xy1<span style="font-weight: bold">[</span><span style="color: red">0</span><span style="font-weight: bold">] - </span>xy2<span style="font-weight: bold">[</span><span style="color: red">0</span><span style="font-weight: bold">]) + </span>abs<span style="font-weight: bold">(</span>xy1<span style="font-weight: bold">[</span><span style="color: red">1</span><span style="font-weight: bold">] - </span>xy2<span style="font-weight: bold">[</span><span style="color: red">1</span><span style="font-weight: bold">])

</span><span style="color: blue; font-weight: bold">def </span>euclideanHeuristic<span style="font-weight: bold">(</span>position<span style="font-weight: bold">, </span>problem<span style="font-weight: bold">, </span>info<span style="font-weight: bold">={}):
    </span><span style="color: red">"The Euclidean distance heuristic for a PositionSearchProblem"
    </span>xy1 <span style="font-weight: bold">= </span>position
    xy2 <span style="font-weight: bold">= </span>problem<span style="font-weight: bold">.</span>goal
    <span style="color: blue; font-weight: bold">return </span><span style="font-weight: bold">( (</span>xy1<span style="font-weight: bold">[</span><span style="color: red">0</span><span style="font-weight: bold">] - </span>xy2<span style="font-weight: bold">[</span><span style="color: red">0</span><span style="font-weight: bold">]) ** </span><span style="color: red">2 </span><span style="font-weight: bold">+ (</span>xy1<span style="font-weight: bold">[</span><span style="color: red">1</span><span style="font-weight: bold">] - </span>xy2<span style="font-weight: bold">[</span><span style="color: red">1</span><span style="font-weight: bold">]) ** </span><span style="color: red">2 </span><span style="font-weight: bold">) ** </span><span style="color: red">0.5

</span><span style="color: green; font-style: italic">#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################

</span><span style="color: blue; font-weight: bold">class </span>CornersProblem<span style="font-weight: bold">(</span>search<span style="font-weight: bold">.</span>SearchProblem<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function
    """

    </span><span style="color: blue; font-weight: bold">def </span>__init__<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>startingGameState<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Stores the walls, pacman's starting position and corners.
        """
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls <span style="font-weight: bold">= </span>startingGameState<span style="font-weight: bold">.</span>getWalls<span style="font-weight: bold">()
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>startingPosition <span style="font-weight: bold">= </span>startingGameState<span style="font-weight: bold">.</span>getPacmanPosition<span style="font-weight: bold">()
        </span>top<span style="font-weight: bold">, </span>right <span style="font-weight: bold">= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls<span style="font-weight: bold">.</span>height<span style="font-weight: bold">-</span><span style="color: red">2</span><span style="font-weight: bold">, </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls<span style="font-weight: bold">.</span>width<span style="font-weight: bold">-</span><span style="color: red">2
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>corners <span style="font-weight: bold">= ((</span><span style="color: red">1</span><span style="font-weight: bold">,</span><span style="color: red">1</span><span style="font-weight: bold">), (</span><span style="color: red">1</span><span style="font-weight: bold">,</span>top<span style="font-weight: bold">), (</span>right<span style="font-weight: bold">, </span><span style="color: red">1</span><span style="font-weight: bold">), (</span>right<span style="font-weight: bold">, </span>top<span style="font-weight: bold">))
        </span><span style="color: blue; font-weight: bold">for </span>corner <span style="color: blue; font-weight: bold">in </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>corners<span style="font-weight: bold">:
            </span><span style="color: blue; font-weight: bold">if not </span>startingGameState<span style="font-weight: bold">.</span>hasFood<span style="font-weight: bold">(*</span>corner<span style="font-weight: bold">):
                </span><span style="color: blue; font-weight: bold">print </span><span style="color: red">'Warning: no food in corner ' </span><span style="font-weight: bold">+ </span>str<span style="font-weight: bold">(</span>corner<span style="font-weight: bold">)
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_expanded <span style="font-weight: bold">= </span><span style="color: red">0 </span><span style="color: green; font-style: italic"># DO NOT CHANGE; Number of search nodes expanded
        # Please add any code here which you would like to use
        # in initializing the problem
        </span><span style="color: red">"*** YOUR CODE HERE ***"

    </span><span style="color: blue; font-weight: bold">def </span>getStartState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Returns the start state (in your state space, not the full Pacman state
        space)
        """
        </span><span style="color: red">"*** YOUR CODE HERE ***"
        </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

    </span><span style="color: blue; font-weight: bold">def </span>isGoalState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Returns whether this search state is a goal state of the problem.
        """
        </span><span style="color: red">"*** YOUR CODE HERE ***"
        </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

    </span><span style="color: blue; font-weight: bold">def </span>getSuccessors<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
            For a given state, this should return a list of triples, (successor,
            action, stepCost), where 'successor' is a successor to the current
            state, 'action' is the action required to get there, and 'stepCost'
            is the incremental cost of expanding to that successor
        """

        </span>successors <span style="font-weight: bold">= []
        </span><span style="color: blue; font-weight: bold">for </span>action <span style="color: blue; font-weight: bold">in </span><span style="font-weight: bold">[</span>Directions<span style="font-weight: bold">.</span>NORTH<span style="font-weight: bold">, </span>Directions<span style="font-weight: bold">.</span>SOUTH<span style="font-weight: bold">, </span>Directions<span style="font-weight: bold">.</span>EAST<span style="font-weight: bold">, </span>Directions<span style="font-weight: bold">.</span>WEST<span style="font-weight: bold">]:
            </span><span style="color: green; font-style: italic"># Add a successor state to the successor list if the action is legal
            # Here's a code snippet for figuring out whether a new position hits a wall:
            #   x,y = currentPosition
            #   dx, dy = Actions.directionToVector(action)
            #   nextx, nexty = int(x + dx), int(y + dy)
            #   hitsWall = self.walls[nextx][nexty]

            </span><span style="color: red">"*** YOUR CODE HERE ***"

        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_expanded <span style="font-weight: bold">+= </span><span style="color: red">1 </span><span style="color: green; font-style: italic"># DO NOT CHANGE
        </span><span style="color: blue; font-weight: bold">return </span>successors

    <span style="color: blue; font-weight: bold">def </span>getCostOfActions<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>actions<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999.  This is implemented for you.
        """
        </span><span style="color: blue; font-weight: bold">if </span>actions <span style="font-weight: bold">== </span><span style="color: blue">None</span><span style="font-weight: bold">: </span><span style="color: blue; font-weight: bold">return </span><span style="color: red">999999
        </span>x<span style="font-weight: bold">,</span>y<span style="font-weight: bold">= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>startingPosition
        <span style="color: blue; font-weight: bold">for </span>action <span style="color: blue; font-weight: bold">in </span>actions<span style="font-weight: bold">:
            </span>dx<span style="font-weight: bold">, </span>dy <span style="font-weight: bold">= </span>Actions<span style="font-weight: bold">.</span>directionToVector<span style="font-weight: bold">(</span>action<span style="font-weight: bold">)
            </span>x<span style="font-weight: bold">, </span>y <span style="font-weight: bold">= </span>int<span style="font-weight: bold">(</span>x <span style="font-weight: bold">+ </span>dx<span style="font-weight: bold">), </span>int<span style="font-weight: bold">(</span>y <span style="font-weight: bold">+ </span>dy<span style="font-weight: bold">)
            </span><span style="color: blue; font-weight: bold">if </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls<span style="font-weight: bold">[</span>x<span style="font-weight: bold">][</span>y<span style="font-weight: bold">]: </span><span style="color: blue; font-weight: bold">return </span><span style="color: red">999999
        </span><span style="color: blue; font-weight: bold">return </span>len<span style="font-weight: bold">(</span>actions<span style="font-weight: bold">)


</span><span style="color: blue; font-weight: bold">def </span>cornersHeuristic<span style="font-weight: bold">(</span>state<span style="font-weight: bold">, </span>problem<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible (as well as consistent).
    """
    </span>corners <span style="font-weight: bold">= </span>problem<span style="font-weight: bold">.</span>corners <span style="color: green; font-style: italic"># These are the corner coordinates
    </span>walls <span style="font-weight: bold">= </span>problem<span style="font-weight: bold">.</span>walls <span style="color: green; font-style: italic"># These are the walls of the maze, as a Grid (game.py)

    </span><span style="color: red">"*** YOUR CODE HERE ***"
    </span><span style="color: blue; font-weight: bold">return </span><span style="color: red">0 </span><span style="color: green; font-style: italic"># Default to trivial solution

</span><span style="color: blue; font-weight: bold">class </span>AStarCornersAgent<span style="font-weight: bold">(</span>SearchAgent<span style="font-weight: bold">):
    </span><span style="color: red">"A SearchAgent for FoodSearchProblem using A* and your foodHeuristic"
    </span><span style="color: blue; font-weight: bold">def </span>__init__<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">):
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchFunction <span style="font-weight: bold">= </span><span style="color: blue; font-weight: bold">lambda </span>prob<span style="font-weight: bold">: </span>search<span style="font-weight: bold">.</span>aStarSearch<span style="font-weight: bold">(</span>prob<span style="font-weight: bold">, </span>cornersHeuristic<span style="font-weight: bold">)
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchType <span style="font-weight: bold">= </span>CornersProblem

<span style="color: blue; font-weight: bold">class </span>FoodSearchProblem<span style="font-weight: bold">:
    </span><span style="color: darkred">"""
    A search problem associated with finding the a path that collects all of the
    food (dots) in a Pacman game.

    A search state in this problem is a tuple ( pacmanPosition, foodGrid ) where
      pacmanPosition: a tuple (x,y) of integers specifying Pacman's position
      foodGrid:       a Grid (see game.py) of either True or False, specifying remaining food
    """
    </span><span style="color: blue; font-weight: bold">def </span>__init__<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>startingGameState<span style="font-weight: bold">):
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>start <span style="font-weight: bold">= (</span>startingGameState<span style="font-weight: bold">.</span>getPacmanPosition<span style="font-weight: bold">(), </span>startingGameState<span style="font-weight: bold">.</span>getFood<span style="font-weight: bold">())
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls <span style="font-weight: bold">= </span>startingGameState<span style="font-weight: bold">.</span>getWalls<span style="font-weight: bold">()
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>startingGameState <span style="font-weight: bold">= </span>startingGameState
        <span style="color: blue">self</span><span style="font-weight: bold">.</span>_expanded <span style="font-weight: bold">= </span><span style="color: red">0 </span><span style="color: green; font-style: italic"># DO NOT CHANGE
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>heuristicInfo <span style="font-weight: bold">= {} </span><span style="color: green; font-style: italic"># A dictionary for the heuristic to store information

    </span><span style="color: blue; font-weight: bold">def </span>getStartState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">):
        </span><span style="color: blue; font-weight: bold">return </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>start

    <span style="color: blue; font-weight: bold">def </span>isGoalState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: blue; font-weight: bold">return </span>state<span style="font-weight: bold">[</span><span style="color: red">1</span><span style="font-weight: bold">].</span>count<span style="font-weight: bold">() == </span><span style="color: red">0

    </span><span style="color: blue; font-weight: bold">def </span>getSuccessors<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: red">"Returns successor states, the actions they require, and a cost of 1."
        </span>successors <span style="font-weight: bold">= []
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_expanded <span style="font-weight: bold">+= </span><span style="color: red">1 </span><span style="color: green; font-style: italic"># DO NOT CHANGE
        </span><span style="color: blue; font-weight: bold">for </span>direction <span style="color: blue; font-weight: bold">in </span><span style="font-weight: bold">[</span>Directions<span style="font-weight: bold">.</span>NORTH<span style="font-weight: bold">, </span>Directions<span style="font-weight: bold">.</span>SOUTH<span style="font-weight: bold">, </span>Directions<span style="font-weight: bold">.</span>EAST<span style="font-weight: bold">, </span>Directions<span style="font-weight: bold">.</span>WEST<span style="font-weight: bold">]:
            </span>x<span style="font-weight: bold">,</span>y <span style="font-weight: bold">= </span>state<span style="font-weight: bold">[</span><span style="color: red">0</span><span style="font-weight: bold">]
            </span>dx<span style="font-weight: bold">, </span>dy <span style="font-weight: bold">= </span>Actions<span style="font-weight: bold">.</span>directionToVector<span style="font-weight: bold">(</span>direction<span style="font-weight: bold">)
            </span>nextx<span style="font-weight: bold">, </span>nexty <span style="font-weight: bold">= </span>int<span style="font-weight: bold">(</span>x <span style="font-weight: bold">+ </span>dx<span style="font-weight: bold">), </span>int<span style="font-weight: bold">(</span>y <span style="font-weight: bold">+ </span>dy<span style="font-weight: bold">)
            </span><span style="color: blue; font-weight: bold">if not </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls<span style="font-weight: bold">[</span>nextx<span style="font-weight: bold">][</span>nexty<span style="font-weight: bold">]:
                </span>nextFood <span style="font-weight: bold">= </span>state<span style="font-weight: bold">[</span><span style="color: red">1</span><span style="font-weight: bold">].</span>copy<span style="font-weight: bold">()
                </span>nextFood<span style="font-weight: bold">[</span>nextx<span style="font-weight: bold">][</span>nexty<span style="font-weight: bold">] = </span><span style="color: blue; font-weight: bold">False
                </span>successors<span style="font-weight: bold">.</span>append<span style="font-weight: bold">( ( ((</span>nextx<span style="font-weight: bold">, </span>nexty<span style="font-weight: bold">), </span>nextFood<span style="font-weight: bold">), </span>direction<span style="font-weight: bold">, </span><span style="color: red">1</span><span style="font-weight: bold">) )
        </span><span style="color: blue; font-weight: bold">return </span>successors

    <span style="color: blue; font-weight: bold">def </span>getCostOfActions<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>actions<span style="font-weight: bold">):
        </span><span style="color: darkred">"""Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999"""
        </span>x<span style="font-weight: bold">,</span>y<span style="font-weight: bold">= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>getStartState<span style="font-weight: bold">()[</span><span style="color: red">0</span><span style="font-weight: bold">]
        </span>cost <span style="font-weight: bold">= </span><span style="color: red">0
        </span><span style="color: blue; font-weight: bold">for </span>action <span style="color: blue; font-weight: bold">in </span>actions<span style="font-weight: bold">:
            </span><span style="color: green; font-style: italic"># figure out the next state and see whether it's legal
            </span>dx<span style="font-weight: bold">, </span>dy <span style="font-weight: bold">= </span>Actions<span style="font-weight: bold">.</span>directionToVector<span style="font-weight: bold">(</span>action<span style="font-weight: bold">)
            </span>x<span style="font-weight: bold">, </span>y <span style="font-weight: bold">= </span>int<span style="font-weight: bold">(</span>x <span style="font-weight: bold">+ </span>dx<span style="font-weight: bold">), </span>int<span style="font-weight: bold">(</span>y <span style="font-weight: bold">+ </span>dy<span style="font-weight: bold">)
            </span><span style="color: blue; font-weight: bold">if </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls<span style="font-weight: bold">[</span>x<span style="font-weight: bold">][</span>y<span style="font-weight: bold">]:
                </span><span style="color: blue; font-weight: bold">return </span><span style="color: red">999999
            </span>cost <span style="font-weight: bold">+= </span><span style="color: red">1
        </span><span style="color: blue; font-weight: bold">return </span>cost

<span style="color: blue; font-weight: bold">class </span>AStarFoodSearchAgent<span style="font-weight: bold">(</span>SearchAgent<span style="font-weight: bold">):
    </span><span style="color: red">"A SearchAgent for FoodSearchProblem using A* and your foodHeuristic"
    </span><span style="color: blue; font-weight: bold">def </span>__init__<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">):
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchFunction <span style="font-weight: bold">= </span><span style="color: blue; font-weight: bold">lambda </span>prob<span style="font-weight: bold">: </span>search<span style="font-weight: bold">.</span>aStarSearch<span style="font-weight: bold">(</span>prob<span style="font-weight: bold">, </span>foodHeuristic<span style="font-weight: bold">)
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>searchType <span style="font-weight: bold">= </span>FoodSearchProblem

<span style="color: blue; font-weight: bold">def </span>foodHeuristic<span style="font-weight: bold">(</span>state<span style="font-weight: bold">, </span>problem<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    Your heuristic for the FoodSearchProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come
    up with an admissible heuristic; almost all admissible heuristics will be
    consistent as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the
    other hand, inadmissible or inconsistent heuristics may find optimal
    solutions, so be careful.

    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a Grid
    (see game.py) of either True or False. You can call foodGrid.asList() to get
    a list of food coordinates instead.

    If you want access to info like walls, capsules, etc., you can query the
    problem.  For example, problem.walls gives you a Grid of where the walls
    are.

    If you want to *store* information to be reused in other calls to the
    heuristic, there is a dictionary called problem.heuristicInfo that you can
    use. For example, if you only want to count the walls once and store that
    value, try: problem.heuristicInfo['wallCount'] = problem.walls.count()
    Subsequent calls to this heuristic can access
    problem.heuristicInfo['wallCount']
    """
    </span>position<span style="font-weight: bold">, </span>foodGrid <span style="font-weight: bold">= </span>state
    <span style="color: red">"*** YOUR CODE HERE ***"
    </span><span style="color: blue; font-weight: bold">return </span><span style="color: red">0

</span><span style="color: blue; font-weight: bold">class </span>ClosestDotSearchAgent<span style="font-weight: bold">(</span>SearchAgent<span style="font-weight: bold">):
    </span><span style="color: red">"Search for all food using a sequence of searches"
    </span><span style="color: blue; font-weight: bold">def </span>registerInitialState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actions <span style="font-weight: bold">= []
        </span>currentState <span style="font-weight: bold">= </span>state
        <span style="color: blue; font-weight: bold">while</span><span style="font-weight: bold">(</span>currentState<span style="font-weight: bold">.</span>getFood<span style="font-weight: bold">().</span>count<span style="font-weight: bold">() &gt; </span><span style="color: red">0</span><span style="font-weight: bold">):
            </span>nextPathSegment <span style="font-weight: bold">= </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>findPathToClosestDot<span style="font-weight: bold">(</span>currentState<span style="font-weight: bold">) </span><span style="color: green; font-style: italic"># The missing piece
            </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actions <span style="font-weight: bold">+= </span>nextPathSegment
            <span style="color: blue; font-weight: bold">for </span>action <span style="color: blue; font-weight: bold">in </span>nextPathSegment<span style="font-weight: bold">:
                </span>legal <span style="font-weight: bold">= </span>currentState<span style="font-weight: bold">.</span>getLegalActions<span style="font-weight: bold">()
                </span><span style="color: blue; font-weight: bold">if </span>action <span style="color: blue; font-weight: bold">not in </span>legal<span style="font-weight: bold">:
                    </span>t <span style="font-weight: bold">= (</span>str<span style="font-weight: bold">(</span>action<span style="font-weight: bold">), </span>str<span style="font-weight: bold">(</span>currentState<span style="font-weight: bold">))
                    </span><span style="color: blue; font-weight: bold">raise </span>Exception<span style="font-weight: bold">, </span><span style="color: red">'findPathToClosestDot returned an illegal move: %s!\n%s' </span><span style="font-weight: bold">% </span>t
                currentState <span style="font-weight: bold">= </span>currentState<span style="font-weight: bold">.</span>generateSuccessor<span style="font-weight: bold">(</span><span style="color: red">0</span><span style="font-weight: bold">, </span>action<span style="font-weight: bold">)
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actionIndex <span style="font-weight: bold">= </span><span style="color: red">0
        </span><span style="color: blue; font-weight: bold">print </span><span style="color: red">'Path found with cost %d.' </span><span style="font-weight: bold">% </span>len<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">.</span>actions<span style="font-weight: bold">)

    </span><span style="color: blue; font-weight: bold">def </span>findPathToClosestDot<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>gameState<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        Returns a path (a list of actions) to the closest dot, starting from
        gameState.
        """
        </span><span style="color: green; font-style: italic"># Here are some useful elements of the startState
        </span>startPosition <span style="font-weight: bold">= </span>gameState<span style="font-weight: bold">.</span>getPacmanPosition<span style="font-weight: bold">()
        </span>food <span style="font-weight: bold">= </span>gameState<span style="font-weight: bold">.</span>getFood<span style="font-weight: bold">()
        </span>walls <span style="font-weight: bold">= </span>gameState<span style="font-weight: bold">.</span>getWalls<span style="font-weight: bold">()
        </span>problem <span style="font-weight: bold">= </span>AnyFoodSearchProblem<span style="font-weight: bold">(</span>gameState<span style="font-weight: bold">)

        </span><span style="color: red">"*** YOUR CODE HERE ***"
        </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

</span><span style="color: blue; font-weight: bold">class </span>AnyFoodSearchProblem<span style="font-weight: bold">(</span>PositionSearchProblem<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    A search problem for finding a path to any food.

    This search problem is just like the PositionSearchProblem, but has a
    different goal test, which you need to fill in below.  The state space and
    successor function do not need to be changed.

    The class definition above, AnyFoodSearchProblem(PositionSearchProblem),
    inherits the methods of the PositionSearchProblem.

    You can use this search problem to help you fill in the findPathToClosestDot
    method.
    """

    </span><span style="color: blue; font-weight: bold">def </span>__init__<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>gameState<span style="font-weight: bold">):
        </span><span style="color: red">"Stores information from the gameState.  You don't need to change this."
        </span><span style="color: green; font-style: italic"># Store the food for later reference
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>food <span style="font-weight: bold">= </span>gameState<span style="font-weight: bold">.</span>getFood<span style="font-weight: bold">()

        </span><span style="color: green; font-style: italic"># Store info for the PositionSearchProblem (no need to change this)
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>walls <span style="font-weight: bold">= </span>gameState<span style="font-weight: bold">.</span>getWalls<span style="font-weight: bold">()
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>startState <span style="font-weight: bold">= </span>gameState<span style="font-weight: bold">.</span>getPacmanPosition<span style="font-weight: bold">()
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>costFn <span style="font-weight: bold">= </span><span style="color: blue; font-weight: bold">lambda </span>x<span style="font-weight: bold">: </span><span style="color: red">1
        </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_visited<span style="font-weight: bold">, </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_visitedlist<span style="font-weight: bold">, </span><span style="color: blue">self</span><span style="font-weight: bold">.</span>_expanded <span style="font-weight: bold">= {}, [], </span><span style="color: red">0 </span><span style="color: green; font-style: italic"># DO NOT CHANGE

    </span><span style="color: blue; font-weight: bold">def </span>isGoalState<span style="font-weight: bold">(</span><span style="color: blue">self</span><span style="font-weight: bold">, </span>state<span style="font-weight: bold">):
        </span><span style="color: darkred">"""
        The state is Pacman's position. Fill this in with a goal test that will
        complete the problem definition.
        """
        </span>x<span style="font-weight: bold">,</span>y <span style="font-weight: bold">= </span>state

        <span style="color: red">"*** YOUR CODE HERE ***"
        </span>util<span style="font-weight: bold">.</span>raiseNotDefined<span style="font-weight: bold">()

</span><span style="color: blue; font-weight: bold">def </span>mazeDistance<span style="font-weight: bold">(</span>point1<span style="font-weight: bold">, </span>point2<span style="font-weight: bold">, </span>gameState<span style="font-weight: bold">):
    </span><span style="color: darkred">"""
    Returns the maze distance between any two points, using the search functions
    you have already built. The gameState can be any game state -- Pacman's
    position in that state is ignored.

    Example usage: mazeDistance( (2,4), (5,6), gameState)

    This might be a useful helper function for your ApproximateSearchAgent.
    """
    </span>x1<span style="font-weight: bold">, </span>y1 <span style="font-weight: bold">= </span>point1
    x2<span style="font-weight: bold">, </span>y2 <span style="font-weight: bold">= </span>point2
    walls <span style="font-weight: bold">= </span>gameState<span style="font-weight: bold">.</span>getWalls<span style="font-weight: bold">()
    </span><span style="color: blue; font-weight: bold">assert not </span>walls<span style="font-weight: bold">[</span>x1<span style="font-weight: bold">][</span>y1<span style="font-weight: bold">], </span><span style="color: red">'point1 is a wall: ' </span><span style="font-weight: bold">+ </span>str<span style="font-weight: bold">(</span>point1<span style="font-weight: bold">)
    </span><span style="color: blue; font-weight: bold">assert not </span>walls<span style="font-weight: bold">[</span>x2<span style="font-weight: bold">][</span>y2<span style="font-weight: bold">], </span><span style="color: red">'point2 is a wall: ' </span><span style="font-weight: bold">+ </span>str<span style="font-weight: bold">(</span>point2<span style="font-weight: bold">)
    </span>prob <span style="font-weight: bold">= </span>PositionSearchProblem<span style="font-weight: bold">(</span>gameState<span style="font-weight: bold">, </span>start<span style="font-weight: bold">=</span>point1<span style="font-weight: bold">, </span>goal<span style="font-weight: bold">=</span>point2<span style="font-weight: bold">, </span>warn<span style="font-weight: bold">=</span><span style="color: blue; font-weight: bold">False</span><span style="font-weight: bold">, </span>visualize<span style="font-weight: bold">=</span><span style="color: blue; font-weight: bold">False</span><span style="font-weight: bold">)
    </span><span style="color: blue; font-weight: bold">return </span>len<span style="font-weight: bold">(</span>search<span style="font-weight: bold">.</span>bfs<span style="font-weight: bold">(</span>prob<span style="font-weight: bold">))
</span>
  </pre>
  </body>
  </html>
  <!--
     FILE ARCHIVED ON 07:41:06 Sep 09, 2016 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 07:21:40 May 28, 2018.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
-->
<!--
playback timings (ms):
  LoadShardBlock: 545.078 (3)
  esindex: 0.01
  captures_list: 600.836
  CDXLines.iter: 15.702 (3)
  PetaboxLoader3.datanode: 294.691 (4)
  exclusion.robots: 0.252
  exclusion.robots.policy: 0.234
  RedisCDXSource: 35.108
  PetaboxLoader3.resolve: 84.167
  load_resource: 129.508
-->
