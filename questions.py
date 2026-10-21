"""
NPTEL Reinforcement Learning - Complete Question Bank (2025 & 2026)
Contains 100% verbatim assignment questions, options, and official solutions/explanations.
"""

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 1 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W1_2026 = [
    {
        "question": "Which of the following is not a useful way to approach a standard multi-armed bandit problem with n arms? Assume bandits are stationary.",
        "options": [
            "“How can I ensure the best action is the one which is mostly selected as time tends to infinity?”",
            "“How can I ensure the total regret as time tends to infinity is minimal?”",
            "“How can I ensure an arm which has an expected reward within a certain threshold of the optimal arm is chosen with a probability above a certain threshold?”",
            "“How can I ensure that when given any 2 arms, I can select the arm with a higher expected return with a probability above a certain threshold?”",
        ],
        "correct": 3,
        "explanation": "Options a, b and c refer to asymptotic correctness, regret optimality and PAC optimality respectively. Option d, i.e., being able to choose the better arm among any 2 arms does not necessarily ensure that we find the optimal arm. For example, if we are given two arms that have very similar and very low expected returns as compared to the optimal arm, it would not be useful to pick those arms again for the purpose of gaining more accurate estimates of the expected reward obtained for picking that arm (which would help in finding the better arm among the two).",
    },
    {
        "question": "What is the decay rate of the weightage given to past rewards in the computation of the Q function in the stationary and non-stationary updates in the multi-armed bandit problem?",
        "options": [
            "hyperbolic, linear",
            "linear, hyperbolic",
            "hyperbolic, exponential",
            "exponential, linear",
        ],
        "correct": 2,
        "explanation": "In the stationary case, the weightage of all rewards given so far is 1/n, where n is the number of rewards obtained for that arm/action so far. Therefore it is hyperbolic. In the non-stationary update, the weightage given to the most recent reward is α, for the pre-update Q value it is 1-α. Upon expansion of the pre-update Q value, we can see that the weightage of the reward in the last but one time step is α(1-α). We can continue to expand in a similar fashion to get that a reward obtained t time steps ago has a weightage of α(1-α)^t (exponential decay).",
    },
    {
        "question": "In the update rule Q_{t+1}(a) ← Q_t(a) + α(R_t - Q_t(a)), select the value of α that we would prefer to estimate Q values in a non-stationary bandit problem.",
        "options": [
            "α = 1 / (n_a + 1)",
            "α = 0.1",
            "α = n_a + 1",
            "α = 1 / (n_a + 1)²",
        ],
        "correct": 1,
        "explanation": "By using a constant value of α, we decrease the importance of past samples exponentially as time progresses, so that our Q value estimates are able to shift as the true action values change. Option (a) weights each sample equally (computing a simple average), preventing meaningful updates when action-values change. Option (c) creates an unbounded sum where estimates grow to infinity. Option (d) weights newer samples lower than case (a).",
    },
    {
        "question": "Assertion: Taking exploratory actions is important for RL agents\nReason: If the rewards obtained for actions are stochastic, an action which gave a high reward once, might give lower reward next time.",
        "options": [
            "Assertion and Reason are both true and Reason is a correct explanation of Assertion",
            "Assertion and Reason are both true and Reason is not a correct explanation of Assertion",
            "Assertion is true and Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 1,
        "explanation": "An RL agent needs to take exploratory actions because it needs to estimate the advantage for each action correctly. So, the Assertion is true. Reason is also true because if the rewards are stochastic, the agent might get high reward once and low reward next time for the same action in the same state. However, even if the rewards obtained for actions were deterministic, the agent still needs to take exploratory actions to figure out more advantageous actions. Hence, Reason does not explain the Assertion correctly.",
    },
    {
        "question": "We are trying different algorithms to find the optimal arm for a multi arm bandit. We plot expected payoff vs time graph for each algorithm for which the expected payoff satisfy some function with respect to time (starting from 0). Which among the following functions will have the least regret. (We know that the optimal expected pay off is 1) (Hint: Plot the functions)",
        "options": [
            "tanh(t)",
            "1 − 2⁻ᵗ",
            "x/20 if x<20, and 1 after that",
            "Same regret for all the above functions.",
        ],
        "correct": 0,
        "explanation": "If we plot the functions we can clearly see the area between y = 1 and f(t). The exact regret will be equal to integral_0^infinity (1 - f(t)) dt. tanh(t) approaches 1 fastest near t=0, giving the minimum area / least regret.",
    },
    {
        "question": "Consider the following statements for ϵ-greedy approach in a non-stationary environment:\ni Keeping a small constant ϵ is a good approach if the environment is non-stationary..\nii Large values of ϵ will lead to unnecessary exploration in the long run.\niii For a stationary environment, decaying ϵ value to zero is a good approach, as after reaching optimality, we would like to reduce exploration.\nWhich of the above statements is/are correct?",
        "options": [
            "ii, iii",
            "only iii",
            "only ii",
            "i, ii",
        ],
        "correct": 3,
        "explanation": "In non-stationary environment since optimal state changes, hence it requires constant exploration to find the optimal state. Decaying epsilon to zero may not find an optimal state; hence, iii is incorrect. Both i and ii are correct.",
    },
    {
        "question": "Following are two ways for defining the probability of selecting an action/arm. Select the option regarding better choice among the following:\n(i) Pr(a_t = a) = Q_t(a) / Σ_a Q_t(a)\n(ii) Pr(a_t = a) = e^{Q_t(a)} / Σ_{b=1}^{n} e^{Q_t(b)}",
        "options": [
            "Both are good as both formulas can bound probability in range 0 to 1.",
            "(i) is better because it is differentiable and requires less complex computation.",
            "None of the above",
        ],
        "correct": 2,
        "explanation": "(a), (b) are incorrect as (i) cannot handle negative values in some cases.",
    },
    {
        "question": "Which of the following best refers to PAC-optimality solution to bandit problems?\nϵ – is the difference between the reward of the chosen arm and true optimal reward\nδ – is the probability that chosen arm is not optimal\nN – is the number of steps to reach PAC-optimality",
        "options": [
            "Given δ and ϵ, minimize the number of steps to reach PAC-optimality(i.e. N)",
            "Given δ and N, minimize ϵ.",
            "Given ϵ and N, maximize the probability of choosing optimal arm(i.e. minimize δ)",
            "none of the above is true about PAC-optimality",
        ],
        "correct": 0,
        "explanation": "refer to the definition of PAC-optimality in Bandit Optimalities video. (Given δ and ϵ, minimize the number of steps to reach PAC-optimality, i.e. N).",
    },
    {
        "question": "Suppose we have a 10-armed bandit problem where the rewards for each of the 10 arms is deterministic and in the range (0, 10). Which among the following methods will allow us to accumulate maximum reward in the long term?",
        "options": [
            "ϵ-greedy with ϵ=0.1.",
            "ϵ-greedy with ϵ=0.01.",
            "greedy with initial reward estimates set to 0.",
            "greedy with initial reward estimates set to 10.",
        ],
        "correct": 3,
        "explanation": "Since the rewards are deterministic, we only need to select each arm once to identify an optimal arm. The greedy method with initial reward higher than all possible rewards ensures that each arm is selected at least once, since on selecting any arm, the resultant reward estimate will necessarily be lower than the initial estimates of the other arms. Once each arm has been selected, the greedy method will settle on the arm with the maximum reward.",
    },
    {
        "question": "Which of the following is/are correct and valid reasons to consider sampling actions from a softmax distribution instead of using an ϵ-greedy approach?\ni Softmax exploration makes the probability of picking an action proportional to the action-value estimates. By doing so, it avoids wasting time exploring obviously 'bad' actions.\nii We do not need to worry about decaying exploration slowly like we do in the ϵ-greedy case. Softmax exploration gives us asymptotic correctness even for a sharp decrease in temperature.\niii It helps us differentiate between actions with action-value estimates (Q values) that are very close to the action with maximum Q value.\nWhich of the above statements is/are correct?",
        "options": [
            "i, ii, iii",
            "only iii",
            "only i",
            "i, ii",
            "i, iii",
        ],
        "correct": 4,
        "explanation": "ii is incorrect. If we decrease temperature too quickly, we could fail to do enough exploration to make correct action-value estimates, just as we would by decaying ϵ too quickly in ϵ-greedy exploration. i and iii are correct. Softmax encourages exploration of actions that have action-value estimates close to the action with maximum Q value. Further concentrated exploration of these actions improves our action-value estimates for them, and this allows us to differentiate between them better.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 1 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W1_2025 = [
    {
        "question": "Which among the following are features of a reinforcement learning solution to a learning problem?",
        "options": [
            "trial and error approach to learning",
            "exploration versus exploitation dilemma",
            "learning based on rewards",
            "absence of any feedback or supervision",
        ],
        "correct": [0, 1, 2],
        "explanation": "The last option is not correct, since rewards act as feedback/supervision for RL agents.",
    },
    {
        "question": "Modelling a living organism as an RL agent, the environment encompasses",
        "options": [
            "everything external to the organism",
            "some portions internal to the organism as well",
        ],
        "correct": 1,
        "explanation": "In living organisms, reward signals are generated within the brain. In the idealised RL framework this is part of the environment.",
    },
    {
        "question": "It was mentioned in the lecture that reinforcement learning solutions have to be able to handle delayed rewards. What exactly is/are the problems that arises due to delayed rewards?",
        "options": [
            "problem in storing rewards",
            "problem in assigning rewards to the actions that caused them",
            "problem in mapping states to the rewards that can be achieved from those states",
        ],
        "correct": [1, 2],
        "explanation": "Different techniques can be used to maintain reward information, so the first option is not really an issue. The next two options do pose challenges to an RL agent. Remember that rewards, in general, depend both on the chosen action and the state in which that action was taken.",
    },
    {
        "question": "In the tic-tac-toe problem, it can be observed that many board positions (states) are symmetric. Assuming an imperfect opponent with a stationary policy/strategy who is also taking advantage of symmetries in the board positions, which of the following statements are true, if we take advantage of symmetries by maintaining a single (probability) value for all symmetric states?",
        "options": [
            "time taken to learn the values reduces",
            "space required to store the values reduces",
            "the final policy learned in this approach is better than the policy learned when not taking advantage of symmetries",
        ],
        "correct": [0, 1],
        "explanation": "Option (b) is obviously true. Option (a) is true because for each value, the experience generated from all corresponding symmetric states are being used to update that value, and hence we can expect faster convergence (when compared to the case where symmetries are being ignored). Option (c) is false because in both cases, given an opponent with a stationary policy, we expect to arrive at the same policy, the difference is only in the time it takes.",
    },
    {
        "question": "Considering again the question of taking advantage of symmetric board positions, is it true, that symmetrically equivalent positions should necessarily have the same value?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "Consider the case where the opponent does not make use of symmetries. Assuming an imperfect opponent, we can consider two states a and b which are symmetrically equivalent. Now, assume that the actions taken by the opponent when in these two states is not symmetrically equivalent. For example, in state a, the opponent may play a sound move, but in state b, the opponent may make a mistake that can be exploited by us. Thus, to be able to best respond to the opponents imperfection as in the above case, it would be beneficial for us to maintain separate values for the states a and b even though they are symmetric.",
    },
    {
        "question": "This question is related to the one discussed in class. Recall the temporal difference learning approach to the tic-tac-toe problem. Suppose that the probability of winning at a particular state is 0.6, the max probability value in the next set of states is 0.8, and based on our exploration policy, we choose a next state which has probability value 0.4. Should you backup the current state’s probability value based on this choice of next state (i.e., move probability value 0.6 closer to 0.4) or not, given that the agent never stops exploring (i.e., the agent always makes an exploratory move some fraction of the time)?",
        "options": [
            "backup the value",
            "do not backup the value",
        ],
        "correct": 0,
        "explanation": "There are valid arguments for both backing up, as well as not backing up values on exploration steps. The argument in favour of backing up is that by backing up values, even on exploration steps, the value function (i.e., the function specifying the value at each state - here, the probability of winning) actually represents the behaviour you are following (because according to your behaviour, you do explore some fraction of the times). The argument against backing up is that exploration is performed only for learning purposes, and that if we were to actually go by our learned policy, say when the agent is deployed in a competition, we will perform only exploitative steps to maximise reward. In this sense, we should only backup values on greedy moves. Now, in the question, we are given that the agent never stops exploring. So, if we choose not to backup the values during exploration steps, we are actually learning a value function (and hence, policy), which is different from the actual policy the agent will follow. Thus, it makes sense to backup the values during all steps.",
    },
    {
        "question": "Suppose we want an RL agent to learn to play the game of golf. For training purposes, we make use of a golf simulator program. Assume that the original reward distribution gives a reward of +10 when the golf ball is hit into the hole and -1 for all other transitions. To aide the agents learning process, we propose to give an additional reward of +3 whenever the ball is within a 1 metre radius of the hole. Is this additional reward a good idea or not? Why?",
        "options": [
            "yes, the additional reward will help speed-up learning",
            "yes, getting the ball to within a metre of the hole is like a sub-goal and hence, should be rewarded",
            "no, the additional reward may actually hinder learning",
            "no, it violates the idea that a goal must be outside the agents direct control.",
        ],
        "correct": 2,
        "explanation": "In this specific case, the additional reward will be detrimental to the learning process, as the agent will learn to accumulate rewards by keeping the ball within the 1 metre radius circle and not actually hitting the ball in the hole. This example highlights the importance of being cautious in setting up the reward function in order to prevent unintended consequences.",
    },
    {
        "question": "Suppose that we are given a 10 armed bandit problem and are also told that the rewards for each arm are deterministic. How many times should each arm be tried before we can identify the best arm with 95% probability?",
        "options": [
            "1",
            "2",
            "95",
            "none of the above",
        ],
        "correct": 0,
        "explanation": "Since we are told that the rewards are deterministic, it is sufficient to pull each arm once and then subsequently pick the arm for which we observed the maximum reward. Note that this is only possible because the rewards were deterministic (i.e., non-stochastic) and also because we knew before hand that the rewards were deterministic.",
    },
    {
        "question": "Suppose that you have been given a number of different drug formulations to treat a particular disease and you job is to identify one among them that best meets certain criteria with regards to its efficacy in treating the disease. Before you run the experiments, you need to provision for the samples that would be required. Treating this as a multi-armed bandit problem, which kind of solution method would you prefer for identifying the best option?",
        "options": [
            "asymptotic correctness",
            "regret optimality",
            "PAC optimality",
        ],
        "correct": 2,
        "explanation": "A PAC optimal solution allows us estimate the number of samples that are required to achieve the required level of performance for the chosen arm.",
    },
    {
        "question": "Suppose we have a 10-armed bandit problem where the rewards for each of the 10 arms is deterministic and in the range (0, 10). Which among the following methods will allow us to accumulate maximum reward in the long term?",
        "options": [
            "ϵ-greedy with ϵ=0.1",
            "ϵ-greedy with ϵ=0.01",
            "greedy with initial reward estimates set to 0",
            "greedy with initial reward estimates set to 10",
        ],
        "correct": 3,
        "explanation": "Since the rewards are deterministic, we only need to select each arm once to identify an optimal arm. The greedy method with initial reward higher than all possible rewards ensures that each arm is selected at least once, since on selecting any arm, the resultant reward estimate will necessarily be lower than the initial estimates of the other arms. Once each arm has been selected, the greedy method will settle on the arm with the maximum reward.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 2 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W2_2026 = [
    {
        "question": "Which of the following statements is NOT true about Thompson Sampling or Posterior Sampling?",
        "options": [
            "After each sample is drawn, the q* distribution for that sampled arm is updated to be closer to the true distribution.",
            "Thompson sampling has been shown to generally give better regret bounds than UCB.",
            "In Thompson sampling, we do not need to eliminate arms each round to get good sample complexity.",
            "The algorithm requires Gaussian priors to represent distributions over q* values for each arm.",
        ],
        "correct": 3,
        "explanation": "We are not constrained to Gaussian priors — any prior distribution can be assumed over the q* values for each arm. Statement (d) is false.",
    },
    {
        "question": "In UCB, the term √(2ln(n)/n_j) is added to each arm’s Q value and the arm with the highest value of this sum is chosen. Which one of the following would definitely happen to the frequency of picking sub-optimal arms when adding √(2ln(n)/n_j²) instead of √(2ln(n)/n_j)?",
        "options": [
            "Sub-optimal arms would be chosen more frequently.",
            "Sub-optimal arms would be chosen less frequently.",
            "Makes no change to the frequency of picking sub-optimal arms.",
            "Sub-optimal arms could be chosen less or more frequently, depending on the samples.",
        ],
        "correct": 3,
        "explanation": "The faster-shrinking uncertainty term means fewer samples needed for confidence, which could mean less wasted exploration (fewer sub-optimal pulls) but could also mean worse estimates earlier leading to more sub-optimal pulls. Either (a) or (b) could be True depending on the problem.",
    },
    {
        "question": "In the proof of the UCB Theorem, when l_i = ⌈8ln(m)/Δᵢ²⌉, q*(a*) - q*(i) - 2·C_{m,l} = 0. Which of the following correctly explains q*(a*) - q*(i) - 2·C_{m,T_i(s_i)} being less than 0 when we replace this fixed value of l by the value T_i(s_i): the number of times the arm i is selected?",
        "options": [
            "T_i(s_i) < l thus C_{m,T_i(s_i)} < C_{m,l}",
            "T_i(s_i) > m thus C_{m,T_i(s_i)} < C_{m,l}",
            "T_i(s_i) > l thus C_{m,T_i(s_i)} < C_{m,l}",
            "T_i(s_i) < l thus C_{m,T_i(s_i)} > C_{m,l}",
        ],
        "correct": 3,
        "explanation": "If the arm is selected fewer times than l, confidence interval is larger: C_{m,T_i(s_i)} > C_{m,l}, which makes q*(a*) - q*(i) - 2·C_{m,T_i(s_i)} < 0.",
    },
    {
        "question": "Which of the following is true about the Median Elimination algorithm?",
        "options": [
            "It is a regret minimizing algorithm.",
            "The probability of the ϵ_l-optimal arms of round l being eliminated is less than δ_l for the round.",
            "It is guaranteed to provide an ϵ-optimal arm at the end.",
            "Replacing ϵ with ϵ/2 in the algorithm doubles the sample complexity.",
        ],
        "correct": 1,
        "explanation": "From the derivation for Median Elimination, the probability of the best arms in a given round being eliminated is bounded by δ_l. Options (a), (c), (d) are incorrect.",
    },
    {
        "question": "We need 8 rounds of median-elimination to get an (ϵ,δ)-PAC arm. Approximately how many samples would have been required using the naive (ϵ,δ)-PAC algorithm given (ϵ,δ) = (1/2, 1/e)? (Choose the value closest to the correct answer)",
        "options": [
            "15000",
            "10000",
            "500",
            "20000",
        ],
        "correct": 0,
        "explanation": "8 rounds ⟹ 2⁸ = 256 arms. Naive algorithm samples = 2k·ln(2k/δ)/ϵ² = 2·256·ln(512e)/(0.25) ≈ 14824 ≈ 15000.",
    },
    {
        "question": "In case of UCB, the regret is generally of the form f(n)+c, where, for the confidence bound given by √(2ln(n)/n_j), f(n) = Σ_{j=1}^{k} (8ln(n)/Δ_j) and c = (1 + π²/3) Σ_{j=1}^{k} Δ_j. What is the form of f(n) for the confidence bound given by √(α·ln(n)/n_j), where α ≥ 2?",
        "options": [
            "Σ_{j=1}^{k} 4α·ln(n)/Δ_j",
            "Σ_{j=1}^{k} 2α²·ln(n)/Δ_j",
            "Σ_{j=1}^{k} α³·ln(n)/Δ_j",
            "Σ_{j=1}^{k} α⁴·ln(n)/(2·Δ_j)",
        ],
        "correct": 0,
        "explanation": "Re-deriving the UCB proof with general α gives f(n) = Σ 4α·ln(n)/Δ_j.",
    },
    {
        "question": "In the naive (ϵ,δ)-PAC algorithm, suppose we draw 2ln(k/δ)/ϵ² samples for each arm instead of 2ln(2k/δ)/ϵ² samples. Using the same analysis presented in the lectures, with what probability can we guarantee that the arm a' returned will have q*(a') value ϵ close to the q* value of the optimal arm?",
        "options": [
            "1 - δ",
            "1 - 4δ",
            "1 - 2δ",
            "1 - δ/2",
        ],
        "correct": 2,
        "explanation": "Using the Chernoff-Hoeffding bounds with the modified sample count, the probability of incorrectly returning a sub-optimal arm is bounded by 2*δ, so the guarantee is 1 - 2*δ.",
    },
    {
        "question": "In median elimination method for obtaining (ϵ,δ)-PAC bounds, which of the following is a plausible update rule for ϵ_l and δ_l if ϵ_1 = ϵ/3 and δ_1 = δ/4?",
        "options": [
            "ϵ_{l+1} = (3/4)*ϵ_l and δ_{l+1} = (4/5)*δ_l",
            "ϵ_{l+1} = (3/4)*ϵ_l and δ_{l+1} = (3/4)*δ_l",
            "ϵ_{l+1} = (2/3)*ϵ_l and δ_{l+1} = (3/4)*δ_l",
            "ϵ_{l+1} = (2/3)*ϵ_l and δ_{l+1} = (4/5)*δ_l",
        ],
        "correct": 2,
        "explanation": "For getting (ϵ,δ)-PAC bounds: sum of ϵ_l <= ϵ and sum of δ_l <= δ. The update ϵ_{l+1} = (2/3)*ϵ_l and δ_{l+1} = (3/4)*δ_l satisfies these conditions.",
    },
    {
        "question": "Suppose we are facing a non-stationary bandit problem. We want to use posterior sampling for picking the correct arm. What is the likely change that needs to be done to the algorithm so that it can adapt to non-stationarity?",
        "options": [
            "Update the posterior rarely.",
            "Randomly shift the posterior drastically from time to time.",
            "Keep adding slight noise to the posterior to prevent its variance from going down quickly.",
            "No change is required.",
        ],
        "correct": 2,
        "explanation": "To adapt to non-stationarity, we must prevent the posterior from collapsing (becoming too certain) while still allowing it to learn from current samples. Adding slight noise achieves this.",
    },
    {
        "question": "In median elimination method for (ϵ,δ)-PAC bounds, we claim that for every phase l, Pr[A ≤ B + ϵ_l] > 1 - δ_l. (S_l – is the set of arms remaining in the lth phase)\nConsider the following statements:\n(i) A – is the maximum of rewards of true best arm in S_l, i.e. in lth phase\n(ii) B – is the maximum of rewards of true best arm in S_{l+1}, i.e. in l+1th phase\n(iii) B – is the minimum of rewards of true best arm in S_{l+1}, i.e. in l+1th phase\n(iv) A – is the minimum of rewards of true best arm in S_l, i.e. in lth phase\n(v) A – is the maximum of rewards of true best arm in S_{l+1}, i.e. in l+1th phase\n(vi) B – is the maximum of rewards of true best arm in S_l, i.e. in lth phase\nWhich of the statements above are correct?",
        "options": [
            "i and ii",
            "iii and iv",
            "iii and iv",
            "v and vi",
            "i and iii",
        ],
        "correct": 0,
        "explanation": "Refer Lemma 1 in the proof for the Median Elimination Algorithm. A is the maximum of rewards of the true best arm in S_l, and B is the maximum of rewards of the true best arm in S_{l+1}.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 2 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W2_2025 = [
    {
        "question": "In the UCB 1 algorithm, how is it ensured that the confidence bounds around the estimated values for each arm shrink?",
        "options": [
            "the intervals do not shrink",
            "the confidence intervals of each arm are made to shrink after every arm selection",
            "in calculating the bounds we use the number of times an arm is selected in the denominator",
            "on selecting an arm its interval is shrunk by half every time",
        ],
        "correct": 2,
        "explanation": "The number of times arm j is selected (n_j) appears in the denominator of the upper confidence bound for each arm. As n_j increases, the bound decreases.",
    },
    {
        "question": "After 12 iterations of the UCB1 algorithm applied on a 4-arm bandit problem, we have n_1=3, n_2=4, n_3=3, n_4=2 and Q_12(1)=0.55, Q_12(2)=0.63, Q_12(3)=0.61, Q_12(4)=0.40. Which arm should be played next?",
        "options": [
            "1",
            "2",
            "3",
            "4",
        ],
        "correct": 3,
        "explanation": "Calculating UCB values: arm 1 = 0.55 + sqrt(2ln12/3) ≈ 1.837; arm 2 = 0.63 + sqrt(2ln12/4) ≈ 1.745; arm 3 = 0.61 + sqrt(2ln12/3) ≈ 1.897; arm 4 = 0.40 + sqrt(2ln12/2) ≈ 1.976. Arm 4 has the highest UCB value.",
    },
    {
        "question": "In the proof of the UCB 1 algorithm, we had the following expression: {min_{0<s<m} (Q_s(a*) + C_{m-1,T_{a*}(s)}) <= max_{l<=s_i<=m} (Q_{s_i}(i) + C_{m-1,T_i(s_i)})}. What does this expression stand for?",
        "options": [
            "the number of instances where the minimum value among the upper confidence bound values of an optimal arm up till the mth time step is less than or equal to the maximum value among the upper confidence bound values of the ith arm between the times steps l and m",
            "the condition that the minimum value among the upper confidence bound values of an optimal arm up till the mth time step is less than or equal to the maximum value among the upper confidence bound values of the ith arm between the times steps l and m",
            "the condition that there exists an upper confidence bound value of an optimal arm that is smaller than the upper confidence bound value of the selected arm i",
            "the number of instances where the upper confidence bound of the optimal arm is smaller than that of the chosen arm i",
        ],
        "correct": 1,
        "explanation": "This expression represents a condition (a boolean event, not a count), specifically that the minimum UCB of the optimal arm up to step m is <= the maximum UCB of arm i between steps l and m.",
    },
    {
        "question": "In the initial stage of the UCB 1 algorithm, each arm is selected one time. Thereafter, the arm that is selected depends on the arm with the maximum upper confidence bound. Suppose that one of the arms has not been selected after its initial selection in the first stage of the algorithm. What happens to the upper confidence bound of this arm?",
        "options": [
            "it increases",
            "it decreases",
            "it remains constant until it is selected",
        ],
        "correct": 0,
        "explanation": "The presence of n (total number of time steps) in the numerator ensures that at each step, n increases while n_j for the unselected arm remains constant, so its upper confidence bound increases.",
    },
    {
        "question": "Suppose that we apply the naive PAC algorithm on a 10-arm bandit problem where the required (ϵ, δ) values are: ϵ = 0.5 and δ = 0.05. How many iterations would the algorithm take to output an arm selection? (Note: each arm is sampled (2/ϵ^2)*ln(2k/δ) times).",
        "options": [
            "48",
            "21",
            "210",
            "480",
        ],
        "correct": 3,
        "explanation": "l = (2/0.25)*ln(20/0.05) = 8*ln(400) ≈ 47.93 ≈ 48 samples per arm. Total iterations across all 10 arms = 10 * 48 = 480.",
    },
    {
        "question": "In the proof of the Naive PAC algorithm, we have the expression: P(Q(a') > Q(a*)) <= P(Q(a') > q*(a') + epsilon/2 OR Q(a*) < q*(a*) - epsilon/2). Why is the LHS 'less than or equal to' the RHS here?",
        "options": [
            "because the occurrence of at least one of the events on the RHS is a necessary but not sufficient condition for the event on the LHS to occur",
            "because the event on the LHS does not require that the events on the RHS occur",
            "because the event on the LHS requires that both the events on the RHS occur",
        ],
        "correct": 0,
        "explanation": "For Q(a') to be greater than Q(a*), at least one of the concentration deviation events on the RHS must occur, making it a necessary condition. Hence P(LHS) <= P(union of RHS events).",
    },
    {
        "question": "Suppose we have a 64-arm bandit problem. We apply the median elimination algorithm where the (ϵ, δ) values are: ϵ = 0.5 and δ = 0.01. How many times do we sample arms in the first round? (Note: in each round, each arm is sampled (1/(ϵ_l^2/2))*ln(3/δ_l) times).",
        "options": [
            "52404",
            "818",
            "52416",
            "819",
        ],
        "correct": 2,
        "explanation": "Round 1: epsilon_1 = epsilon/4 = 0.125, delta_1 = delta/2 = 0.005. Samples per arm = (1/(0.125^2/2))*ln(3/0.005) = (2/0.015625)*ln(600) = 128*6.3969 ≈ 819. Total samples across 64 arms = 64 * 819 = 52416.",
    },
    {
        "question": "Continuing with the previous example, what is the number of samples in the third round? Also, what is the total number of rounds required to identify the (ϵ, δ)-optimal arm?",
        "options": [
            "50384, 6",
            "50384, 7",
            "50378, 6",
            "201514, 7",
        ],
        "correct": 0,
        "explanation": "Round 3: 16 arms remain. epsilon_3 = (3/4)^2 * (0.5/4) = 9/16 * 0.125; delta_3 = delta/8 = 0.00125. Samples per arm = 3149. Total samples = 16 * 3149 = 50384. Number of rounds = log2(64) = 6.",
    },
    {
        "question": "Consider a bandit problem in which there is a single optimal arm, a*. Applying the median elimination algorithm to this problem, is it possible that arm a* is eliminated in the first round? In case it is possible, does this mean that the algorithm cannot output an arm that is epsilon-close to a*?",
        "options": [
            "no",
            "yes, no",
            "yes, yes",
        ],
        "correct": 1,
        "explanation": "Yes, it is possible for a* to be eliminated if its sample mean falls below the median. However, this does not mean the algorithm cannot output an arm that is epsilon-close to a*, as the probability of eliminating all epsilon-optimal arms is bounded by delta_l.",
    },
    {
        "question": "We know that there is an exploration/exploitation dilemma in reinforcement learning problems. Considering the Thompson sampling algorithm for solving bandit problems, which step of the algorithm ensures that we perform exploration?",
        "options": [
            "initialisation of each arm's reward distribution",
            "updating the reward distribution based on observing actual reward for an arm",
            "sampling the expected payoff of each arm from the corresponding reward distribution",
            "identifying the correct arm given the set of expected payoffs for each arm sampled from each arm's reward distribution",
        ],
        "correct": 2,
        "explanation": "Sampling from the posterior distribution generates stochastic estimates: arms with lower means but higher uncertainty can still sample high values, driving exploration.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 3 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W3_2026 = [
    {
        "question": "Which of the following is true for an MDP?",
        "options": [
            "Pr(s_{t+1}, r_{t+1} | s_t, a_t) = Pr(s_{t+1}, r_{t+1})",
            "Pr(s_{t+1}, r_{t+1} | s_t, a_t, s_{t-1}, a_{t-1}, s_{t-2}, a_{t-2}, ..., s_0, a_0) = Pr(s_{t+1}, r_{t+1} | s_t, a_t)",
            "Pr(s_{t+1}, r_{t+1} | s_t, a_t) = Pr(s_{t+1}, r_{t+1} | s_0, a_0)",
            "Pr(s_{t+1}, r_{t+1} | s_t, a_t) = Pr(s_t, r_t | s_{t-1}, a_{t-1})",
        ],
        "correct": 1,
        "explanation": "(b) is true for any MDP. (a),(c) and (d) are not true.",
    },
    {
        "question": "The baseline in the REINFORCE update should not depend on which of the following (without voiding any of the steps in the proof of REINFORCE)?",
        "options": [
            "r_{n-1}",
            "r_n",
            "Action taken(a_n)",
            "None of the above",
        ],
        "correct": 2,
        "explanation": "The baseline must not depend on any action. The baseline can depend on current and past rewards. An example baseline is given in the videos where the average of rewards obtained so far is considered to be the baseline.",
    },
    {
        "question": "In many supervised machine learning algorithms, such as neural networks, we rely on the gradient descent technique. However, in the policy gradient approach to bandit problems, we made use of gradient ascent. This discrepancy can mainly be attributed to the differences in",
        "options": [
            "the objectives of the learning tasks",
            "the parameters of the functions whose gradient are being calculated",
            "the nature of the feedback received by the algorithms",
        ],
        "correct": [0, 2],
        "explanation": "The feedback in most supervised learning algorithms is an error signal which we wish to minimise. Hence, we would look to perform gradient descent. In policy gradient, we are trying to maximise the reward signal, hence gradient ascent.",
    },
    {
        "question": "In case of linear bandits, let’s consider we have 2 actions - a_1 and a_2. The policy π to be followed when encountering a state s is given by:\nπ(a_1|s) = e^{w_1^T s} / (e^{w_1^T s} + e^{w_2^T s})\nπ(a_2|s) = e^{w_2^T s} / (e^{w_1^T s} + e^{w_2^T s})\nwhere w_1 and w_2 are weight vectors associated with a_1 and a_2 respectively. If we are using REINFORCE to learn the parameters, what will be the update for w_1 and w_2, when we pull action a_1?\n(i) w_1 -> w_1 + α r (s - (e^{w_1^T s} / (e^{w_1^T s} + e^{w_2^T s})) s)\n(ii) w_1 -> w_1 + α r (- (e^{w_1^T s} / (e^{w_1^T s} + e^{w_2^T s})) s)\n(iii) w_2 -> w_2 + α r (s - (e^{w_2^T s} / (e^{w_1^T s} + e^{w_2^T s})) s)\n(iv) w_2 -> w_2 + α r (- (e^{w_2^T s} / (e^{w_1^T s} + e^{w_2^T s})) s)\nWhich of the above updates are correct?",
        "options": [
            "(i), (iii)",
            "(i), (iv)",
            "(ii), (iii)",
            "(ii), (iv)",
        ],
        "correct": 1,
        "explanation": "Derive the update using the REINFORCE formula: w_1 uses positive gradient term (i) and w_2 uses negative gradient term (iv).",
    },
    {
        "question": "The update in REINFORCE is given by θ_{t+1} = θ_t + α r_t ∂lnπ(a_t; θ_t)/∂θ_t, where r_t ∂lnπ(a_t; θ_t)/∂θ_t is an unbiased estimator of the true gradient of the performance function. However, there was another variant of REINFORCE, where a baseline b, that is independent of the action taken, is subtracted from the obtained reward, i.e., the update is given by θ_{t+1} = θ_t + α(r_t - b) ∂lnπ(a_t; θ_t)/∂θ_t.\nHow are E[(r_t - b) ∂lnπ(a_t; θ_t)/∂θ_t] and E[r_t ∂lnπ(a_t; θ_t)/∂θ_t] related?",
        "options": [
            "E[(r_t - b) ∂lnπ(a_t; θ_t)/∂θ_t] = E[r_t ∂lnπ(a_t; θ_t)/∂θ_t]",
            "E[(r_t - b) ∂lnπ(a_t; θ_t)/∂θ_t] < E[r_t ∂lnπ(a_t; θ_t)/∂θ_t]",
            "E[(r_t - b) ∂lnπ(a_t; θ_t)/∂θ_t] > E[r_t ∂lnπ(a_t; θ_t)/∂θ_t]",
            "Could be either of a, b or c, depending on the choice of baseline",
        ],
        "correct": 0,
        "explanation": "E[b ∂lnπ(a_t;θ_t)/∂θ_t] = E[b (1/π(a_t;θ_t)) ∂π(a_t;θ_t)/∂θ_t] = sum_a b ∂π(a;θ_t)/∂θ_t = b ∂(sum_a π(a;θ_t))/∂θ_t = b ∂(1)/∂θ_t = 0. Thus, E[(r_t - b) ∂lnπ(a_t; θ_t)/∂θ_t] = E[r_t ∂lnπ(a_t; θ_t)/∂θ_t].",
    },
    {
        "question": "Consider the following policy-search algorithm for a multi-armed binary bandit:\n∀a, π_{t+1}(a) = π_t(a)(1 - α) + α(1_{a=a_t} r_t + (1 - 1_{a=a_t})(1 - r_t))\nwhere 1_{a=a_t} is 1 if a_t = a and 0 otherwise. Which of the following is true for the above algorithm?",
        "options": [
            "It is L_{R-I} algorithm.",
            "It is L_{R-ϵP} algorithm.",
            "It would work well if the best arm had probability of 0.9 of resulting in +1 reward and the next best arm had probability of 0.5 of resulting in +1 reward",
            "It would work well if the best arm had probability of 0.3 of resulting in +1 reward and the worst arm had probability of 0.25 of resulting in +1 reward",
        ],
        "correct": 2,
        "explanation": "The given algorithm is L_{R=P} algorithm. It would work well for the case described in (c) as it gives equal weightage to penalties and rewards, and as the gap between best arm and next best arm’s probability of giving +1 reward is significant, it would easily figure out the best arm.",
    },
    {
        "question": "The actions in contextual bandits do not determine the next state, but typically do in full RL problems. True or false?",
        "options": [
            "True",
            "False",
        ],
        "correct": 0,
        "explanation": "Refer to the contextual bandits lecture. Contextual bandits do not determine subsequent state/context, but actions in full RL MDPs do.",
    },
    {
        "question": "In a continuous action space environment, we can employ any value function-based algorithm to discover an optimal policy.",
        "options": [
            "True",
            "False",
        ],
        "correct": 1,
        "explanation": "When the action space is continuous, storing values for each action is hard in the case of value function-based methods. Due to the action approximation for the continuous actions, it is necessary to optimize the action space for every action chosen from the policy, to find the estimated optimal action. This approach is slow, and policy gradient-based methods are likely to generalize better.",
    },
    {
        "question": "Let’s assume for some full RL problem we are acting according to a policy π. At some time t, we are in a state s where we took action a_1. After few time steps, at time t′, the same state s was reached where we performed an action a_2 (≠ a_1). Which of the following statements is true?",
        "options": [
            "π is definitely a stationary policy",
            "π is definitely a non-stationary policy",
            "π can be stationary or non-stationary.",
        ],
        "correct": 2,
        "explanation": "A stationary policy can be stochastic and thus for the same state different actions can be chosen at different time steps. Thus π can be stationary or non-stationary policy.",
    },
    {
        "question": "In solving a multi-arm bandit problem using the policy gradient method, are we assured of converging to the optimal solution?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "Depending upon the properties of the function whose gradient is being ascended, the policy gradient approach may converge to a local optimum.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 3 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W3_2025 = [
    {
        "question": "In solving a multi-arm bandit problem using the policy gradient method, are we assured of\nconverging to the optimal solution?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "Depending upon the properties of the function whose gradient is being ascended, the policy\ngradient approach may converge to a local optimum.",
    },
    {
        "question": "In many supervised machine learning algorithms, such as neural networks, we rely on the\ngradient descent technique. However, in the policy gradient approach to bandit problems, we\nmade use of gradient ascent. This discrepancy can mainly be attributed to the differences in",
        "options": [
            "the objectives of the learning tasks",
            "the parameters of the functions whose gradient are being calculated",
            "the nature of the feedback received by the algorithms",
        ],
        "correct": 2,
        "explanation": "The feedback in most supervised learning algorithms is an error signal which we wish to\nminimise. Hence,wewouldlooktoperformgradientdescent. Inpolicygradient,wearetrying\nto maximise the reward signal, hence gradient ascent.",
    },
    {
        "question": "Consider a bandit problem in which the parameters on which the policy depends are the\npreferencesoftheactionsandtheactionselectionprobabilitiesaredeterminedbythesoftmax\nrelationshipasπ(a )= eθi ,wherek isthetotalnumberofactionsandθ isthepreference\ni (cid:80)k eθj i\nj=1\nvalue of action a . Derive the parameter update conditions according to the REINFORCE\ni\nprocedure considering the above described parameters and where the baseline is the reference\nreward defined as the average of the rewards received for all arms.",
        "options": [
            "∆θ =α(R−b)(1−π(a ;θ))\ni i",
            "∆θ =α(R−b) eθi\ni (cid:80)k eθj\nj=1",
            "∆θ =α(R−b)(π(a ;θ)−1)\ni i",
            "∆θ =α(R−b) 1−eθi\ni (cid:80)k eθj\nj=1",
        ],
        "correct": 0,
        "explanation": "According to the REINFORCE method, at each step, we update the parameter as\n∂lnπ(a ;θ)\n∆θ =α(R −b ) n\nn n n ∂θ\nn\nConsidering the softmax preferences, the characteristic eligibility is\n∂lnπ(a n;θ)\n=\n∂\nln\neθi\n=\n∂\n(θ\n−ln((cid:88)k\neθj))=1−π(a ;θ)\n∂θ n ∂θ n (cid:80)k eθj ∂θ n n i\nj=1 j=1\nConsidering the baseline, b as the average of all rewards seen so far, and α as the step size\nparameter, the update conditions are\n∆θ =α(R−b)(1−π(a ;θ))\ni i",
    },
    {
        "question": "Repeattheaboveproblemforthecasewheretheparametersarethemeanandvarianceofthe\nnormal distribution according to which the actions are selected and the baseline is zero.\n( ) (cid:110) (cid:111)",
        "options": [
            "∆µ =α r an−µn ;∆σ =α r (an−µn)2 −1\nn n n σn n n n σ n2",
            "∆µ\nn\n=α nr n( an σ− 2µn) ;∆σ\nn\n=α nr n(cid:110) (an−µ σn 2)2−σ n2(cid:111)\nn n",
            "∆µ\nn\n=α nr n( an σ− 2µn) ;∆σ\nn\n=α nr n(cid:110) (an−µ σn 3)2−σ n2(cid:111)\nn n\n( ) (cid:110) (cid:111)",
            "∆µ =α r an−µn ;∆σ =α r (an−µn)2−σ\nn n n σn n n n σ n2",
        ],
        "correct": 2,
        "explanation": "Assuming parameters to be µ and σ, we have policy,\nπ(a;µ,σ2)= √1 e−(a− 2σµ)2\n2πσ\nFor the mean:\n∂lnπ(a ;µ ,σ ) ∂\n(cid:26)\n(a −µ\n)2(cid:27)\na −µ\nn n n = − n n = n n\n∂µ ∂µ 2σ2 σ2\nn n n n\nFor the variance:\n∂lnπ(a n;µ n,σ n)\n=\n∂ (cid:8) −ln(√\n2πσ\n)(cid:9)\n+\n∂ (cid:26) −(a n−µ n)2(cid:27)\n∂σ ∂σ n ∂σ 2σ2\nn n n n\nSolving, we have:\n∂lnπ(a ;µ ,σ ) 1 (a −µ )2 1 (cid:18) a −µ (cid:19)2\nn n n =− + n n = { n n −1}\n∂σ σ σ3 σ σ\nn n n n n\nThus, the updates are:\n(cid:18) (cid:19)\na −µ\nµ =µ +α r n n\nn+1 n n n σ2\nn\n1\n(cid:40)(cid:18)\na −µ\n(cid:19)2 (cid:41)\nσ =σ +α r n n −1\nn+1 n n nσ σ\nn n",
    },
    {
        "question": "Which among the following is/are differences between contextual bandits and full RL problems?",
        "options": [
            "the actions and states in contextual bandits share features, but not in full RL problems",
            "the actions in contextual bandits do not determine the next state, but typically do in full RL problems",
            "full RL problems can be modelled as MDPs whereas contextual bandit problems cannot",
            "no difference",
        ],
        "correct": 1,
        "explanation": "Option (a) is not true because we can think of representations where actions and states share\nfeatures. Similarly,option(c)isfalsebecausecontextualbanditproblemscanalsobemodelled\nas MDPs.",
    },
    {
        "question": "Given a stationary policy, is it possible that if the agent is in the same state at two different\ntime steps, it can choose two different actions?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "A stationary policy does not mean that the policy is deterministic. For example, for state\ns and actions a and a , a stationary policy π may have π(a |s ) = 0.4 and π(a |s ) = 0.6.\n1 1 2 1 1 2 1\nThus, at different time steps, if the agent is in the same state s , it may perform either of the\n1\ntwo actions.",
    },
    {
        "question": "In class we saw that it is possible to learn via a sequence of stationary policies, i.e., during an\nepisode, the policy does not change, but we move to a different stationary policy before the\nnext episode begins. Does the temporal difference method encountered when discussing the\ntic-tac-toe example follow this pattern of learning?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "Recall that within an episode, at each step, after observing a reward, we modify the value\nfunction (the probability values in the tic-tac-toe example). Since the policy used to select\nactions is derived from the value function, in effect we are modifying the policy at each step.",
    },
    {
        "question": "Wesawthefollowingdefinitionoftheaction-valuefunctionforpolicyπ: q (s,a)=E [G |S =\nπ π t t\ns,A =a]. Suppose that the action selected according to the policy π in state s is a . For the\nt 1\nsame state, will the function be defined for actions other than a ?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "The interpretation of the action-value function q (s,a)= E [G |S = s,A = a] is the expec-\nπ π t t t\ntationofthereturngiventhatwetakeactionainstatesattimetandthereafterselectactions\nbased on policy π. Thus, the only constraint for the actions is that they must be applicable\nin state s.",
    },
    {
        "question": "Consider a 100x100 grid world domain where the agent starts each episode in the bottom-left\ncorner, and the goal is to reach the top-right corner in the least number of steps. To learn an\noptimal policy to solve this problem you decide on a reward formulation in which the agent\nreceives a reward of +1 on reaching the goal state and 0 for all other transitions. Suppose\nyou try two variants of this reward formulation, (P ), where you use discounted returns with\n1\nγ ∈ (0,1), and (P ), where no discounting is used. Which among the following would you\n2\nexpect to observe?",
        "options": [
            "the same policy is learned in (P ) and (P )\n1 2",
            "no learning in (P )",
            "no learning in (P )",
            "policy learned in (P ) is better than the policy learned in (P )\n2 1",
        ],
        "correct": 2,
        "explanation": "In (P ), since there is no discounting, the return for each episode regardless of the number of\n2\nstepsis+1. Thispreventstheagentfromlearningapolicywhichtriestominimisethenumber\nof steps to reach the goal state. In (P ), the discount factor ensures that the longer the agent\n1\ntakes to reach the goal state, the lesser reward it gets. This motivates the agent to find take\nthe shortest path to the goal state.",
    },
    {
        "question": "Given an MDP with finite state set, S, and an arbitrary function, f, that maps S to the real\nnumbers, the MDP has a policy π such that f =Vπ.",
        "options": [
            "false",
            "true",
        ],
        "correct": 0,
        "explanation": "Consider an MDP where all rewards are 0.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 4 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W4_2026 = [
    {
        "question": "State True/False\nThe state transition graph for any MDP is a directed acyclic graph.",
        "options": [
            "True",
            "False",
        ],
        "correct": 1,
        "explanation": "The statement is false. There is a possibility of transitioning to the same state, as well as having other cycles.",
    },
    {
        "question": "Consider the following statements:\n(i) The optimal policy of an MDP is unique.\n(ii) We can determine an optimal policy for a MDP using only the optimal value function(v*), without accessing the MDP parameters.\n(iii) We can determine an optimal policy for a given MDP using only the optimal q-value function(q*), without accessing the MDP parameters.\nWhich of these statements are true?",
        "options": [
            "Only (ii)",
            "Only (iii)",
            "Only (i), (ii)",
            "Only (i), (iii)",
            "Only (ii), (iii)",
        ],
        "correct": 1,
        "explanation": "Optimal policy can be recovered from an optimal q-value function. Also, a given MDP can have multiple optimal policies.",
    },
    {
        "question": "Which of the following is a benefit of using RL algorithms for solving MDPs?",
        "options": [
            "They do not require the state of the agent for solving a MDP.",
            "They do not require the action taken by the agent for solving a MDP.",
            "They do not require the state transition probability matrix for solving a MDP.",
            "They do not require the reward signal for solving a MDP.",
        ],
        "correct": 2,
        "explanation": "RL algorithms require to know the state the agent is in, the action it takes and a reward signal from the environment to solve the MDP. However, they do not need to know the state transition probability matrix.",
    },
    {
        "question": "Consider the following equations:\n(i) vπ(s) = E_π [Σ_{i=t}^{∞} γ^{i-t} R_{i+1} | S_t = s]\n(ii) qπ(s,a) = Σ_{s'} p(s'|s,a) vπ(s')\n(iii) vπ(s) = Σ_a π(a|s) qπ(s,a)\nWhich of the above are correct?",
        "options": [
            "Only (i)",
            "Only (i), (ii)",
            "Only (ii), (iii)",
            "Only (i), (iii)",
            "(i), (ii), (iii)",
        ],
        "correct": 3,
        "explanation": "(i) is the definition of vπ(s) and (iii) follows from definition of vπ(s) and qπ(s,a). (ii) doesn’t contain the immediate reward term and hence is wrong.",
    },
    {
        "question": "State True/False\nWhile solving MDPs, in case of discounted rewards, the value of γ(discount factor) cannot affect the optimal policy.",
        "options": [
            "True",
            "False",
        ],
        "correct": 1,
        "explanation": "With the change in γ value, the expected return of any state could change and thus, the optimal policy could change.",
    },
    {
        "question": "Consider the following statements for a finite MDP (I is an identity matrix with dimensions |S|×|S|(S is the set of all states) and P_π is a stochastic matrix):\n(i) MDP with stochastic rewards may not have a deterministic optimal policy.\n(ii) There can be multiple optimal stochastic policies.\n(iii) If 0≤γ <1, then rank of the matrix I−γP_π is equal to |S|.\n(iv) If 0≤γ <1, then rank of the matrix I−γP_π is less than |S|.\nWhich of the above statements are true?",
        "options": [
            "Only (ii), (iii)",
            "Only (ii), (iv)",
            "Only (i), (iii)",
            "Only (i), (ii), (iii)",
        ],
        "correct": 0,
        "explanation": "Check the lectures, it states that there always exists a deterministic optimal policy. Lectures provide an example of multiple stochastic optimal policies. I−γP_π will have non zero eigenvalues, so the rank will be equal to the number of rows which is |S|.",
    },
    {
        "question": "Consider an MDP with 3 states A, B, C. From each state, we can go to either of the two states, i.e, from state A, we can perform 2 actions, that lead to state B and C respectively. The rewards for all the transitions are: r(A,B)=2 (reward if we go from A to B), r(B,A)=5, r(B,C)=7, r(C,B)=10, r(A,C)=1, r(C,A)=12. The discount factor is 0.7. Find the value function for the policy given by: π(A) = C (if we are in state A, we choose the action to go to C), π(B)=A and π(C)=B ([vπ(A),vπ(B),vπ(C)]).",
        "options": [
            "[10.2, 16.7, 20.2]",
            "[14.2, 16.5, 15.1]",
            "[15.9, 16.1, 21.3]",
            "[12.2, 6.2, 14.5]",
        ],
        "correct": 2,
        "explanation": "We can just substitute the options to find out which one is a fixed point of the Bellman equation, alternatively, compute (I−γP_π)^{-1} r_π. Note: P_π = [[0,0,1],[1,0,0],[0,1,0]] ; r_π = [1,5,10]^T ; γ = 0.7.",
    },
    {
        "question": "Suppose x is a fixed point for the function A, y is a fixed point for the function B, and x = BA(x), where BA is the composition of B and A. Consider the following statements:\n(i) x is a fixed point for B\n(ii) x=y\n(iii) BA(y)=y\nWhich of the above must be true?",
        "options": [
            "Only (i)",
            "Only (ii)",
            "Only (i), (ii)",
            "(i), (ii), (iii)",
        ],
        "correct": 0,
        "explanation": "x=B(A(x)) => x=B(x). Therefore, x is a fixed point of B. However, that does not mean x=y. The function B could have multiple fixed points (consider the identity function), so (ii) is False. There is no guarantee that y is a fixed point for A. So, we cannot say (iii) is True.",
    },
    {
        "question": "Which of the following is not a valid norm function? (x is a D-dimensional vector)",
        "options": [
            "max_{d ∈ {1,...,D}} |x_d|",
            "√(Σ_{d=1}^{D} x_d²)",
            "min_{d ∈ {1,...,D}} |x_d|",
            "Σ_{d=1}^{D} |x_d|",
        ],
        "correct": 2,
        "explanation": "(c) can be zero when x is not the zero vector.",
    },
    {
        "question": "Which of the following is a contraction mapping in any norm?",
        "options": [
            "T([x_1, x_2]) = [0.5 x_1, 0.5 x_2]",
            "T([x_1, x_2]) = [2 x_1, 2 x_2]",
            "T([x_1, x_2]) = [2 x_1, 3 x_2]",
            "T([x_1, x_2]) = [x_1 + x_2, x_1 - x_2]",
        ],
        "correct": 0,
        "explanation": "(a) is a contraction mapping in any norm as ||Tu - Tv|| = 0.5 ||u - v||.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 4 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W4_2025 = [
    {
        "question": "You receive the following letter:\n\nDear Friend,\nSometime ago, I bought this old house, but found it to be haunted by ghostly sardonic laughter. As a result it is hardly habitable. There is hope, however, for by actual testing I have found that this haunting is subject to certain laws, obscure but infallible, and that the laughter can be affected by my playing the organ or burning incense. In each minute, the laughter occurs or not, it shows no degree. What it will do during the ensuing minute depends, in the following exact way, on what has been happening during the preceding minute:\nWhenever there is laughter, it will continue in the succeeding minute unless I play the organ, in which case it will stop. But continuing to play the organ does not keep the house quiet. I notice, however, that whenever I burn incense when the house is quiet and do not play the organ it remains quiet for the next minute.\nAt this minute of writing, the laughter is going on. Please tell me what manipulations of incense and organ I should make to get that house quiet, and to keep it so.\nSincerely, At Wits End\n\nAssume that we make the following decisions in formulating this problem as an MDP:\nState set: {L, Q}, where L indicates that there is laughter in the room, and Q indicates that the room is quiet.\nAction set: {O∧I, O∧¬I, ¬O∧I, ¬O∧¬I}, where O corresponds to playing the organ, and I corresponds to burning incense.\nWe consider this as a continuing discounted problem with γ = 0.9 and we let the reward be +1 on any transition into the silent state, and -1 on any transition into the laughing state.\nAssuming deterministic state transitions and rewards based upon current state and action, which among the following 4-tuples (current state, action, next state, reward) represent correct state transitions and rewards?",
        "options": [
            "(L, O∧I, Q, +1)",
            "(L, O∧¬I, L, -1)",
            "(L, ¬O∧I, Q, +1)",
            "(L, ¬O∧¬I, L, -1)",
            "(Q, O∧I, Q, +1)",
            "(Q, O∧¬I, L, -1)",
            "(Q, ¬O∧I, Q, +1)",
            "(Q, ¬O∧¬I, L, -1)",
        ],
        "correct": [0, 3, 5, 6, 7],
        "explanation": "We know that if there is laughter and the organ is played, then in the next step laughter will stop. This contradicts option (b). Similarly, option (c) indicates that by burning incense alone laughter can be made to stop, which is incorrect. Option (e) is also not correct because we know that playing the organ when the house is quiet does not result in the house staying quiet.",
    },
    {
        "question": "Based on the problem described in the previous question, what advice would you give your friend?",
        "options": [
            "If there is laughter, play the organ and burn incense; if the room is quiet, play the organ and burn incense.",
            "Never play the organ; always burn incense.",
            "Always play the organ; never burn incense.",
            "If there is laughter, play the organ; if the room is quiet, do not play the organ and burn incense.",
        ],
        "correct": 3,
        "explanation": "Option (d) will ensure that the house will enter the quiet state in the next step (since the organ is played while there is laughter) and will remain in the quiet state from then on (since incense is burnt without the organ being played when the house is quiet). In fact, the state transitions and rewards will be: (L, O∧¬I, Q, +1), (Q, ¬O∧I, Q, +1), (Q, ¬O∧I, Q, +1), ... Thus, cumulative return will be: +1 + γ(+1) + γ^2(+1) + ... = 1/(1-γ) = 1/(1-0.9) = 10, which is the maximum possible return.",
    },
    {
        "question": "If a policy is greedy with respect to its own value function, then it is an optimal policy.",
        "options": [
            "false",
            "true",
        ],
        "correct": 1,
        "explanation": "Consider the value function corresponding to an arbitrary policy π. If we derive a policy that is greedy with respect to this value function, by the policy improvement theorem, the new policy is strictly better than the old policy, unless the old policy was itself an optimal policy.",
    },
    {
        "question": "Consider a 4 X 4 grid world problem where the goal is to reach either the top left corner or the bottom right corner. The agent can choose from four actions {up, down, left, right} which deterministically cause the corresponding state transitions, except that actions that would take the agent off the grid leave the state unchanged. All transitions result in a reward of -1 until a terminal state is reached. If the agent follows an equiprobable random policy, what will be the missing values in the first and second row respectively? (v_π for gridworld)",
        "options": [
            "-20, -14",
            "-14, -20",
            "-14, -18",
            "-20, -18",
        ],
        "correct": 1,
        "explanation": "Using Bellman equation for first row: v(s) = 0.25*(-1+v(s)-1-21-19) = 0.25v(s)-10.5 => v(s)=-14. For second row: v(s) = 0.25*(-1+v(s)-23-21-15) => v(s)=-20.",
    },
    {
        "question": "If π is the equiprobable random policy, what are the respective values of q_π(s_1, down) and q_π(s_2, down) given that s_1 is the last cell in the third row (value -14) and s_2 is the last cell in the second row?",
        "options": [
            "-1, -15",
            "-15, -21",
            "0, -14",
            "-13, -19",
        ],
        "correct": 0,
        "explanation": "For s_1, moving down transitions to the terminal state (value 0) with reward -1, giving q_π(s_1, down) = -1 + 0 = -1. For s_2, moving down transitions to s_1 (value -14) with reward -1, giving q_π(s_2, down) = -1 + (-14) = -15.",
    },
    {
        "question": "In a particular grid-world example, rewards are positive for goals, negative for running into the edge of the world, and zero the rest of the time. Are the signs of these rewards important, or only the intervals between them? Prove, using the discounted return equation G_t = Σ_{k=0}^{∞} γᵏ R_{t+k+1}, that adding a constant C to all rewards adds a constant K to the values of all states. What is K in terms of C and γ?",
        "options": [
            "K = 1 / (C(1 - γ))",
            "K = C(1/(1-γ) - 1)",
            "K = C(1/(1-γ) + 1)",
            "K = C / (1 - γ)",
        ],
        "correct": 3,
        "explanation": "G'_t = Σ_{k=0}^{∞} γᵏ (R_{t+k+1} + C) = Σ_{k=0}^{∞} γᵏ R_{t+k+1} + C Σ_{k=0}^{∞} γᵏ = G_t + C / (1 - γ). Thus, K = C / (1 - γ).",
    },
    {
        "question": "Given a reinforcement learning problem, algorithm A will return the optimal state value function for that problem and algorithm B will return the optimal action value function. Your aim is to use the value function so obtained to behave optimally in the environment. Assuming that you know the expected rewards for each state transition, but not the state transition probabilities, which algorithm’s output would you prefer to use?",
        "options": [
            "Algorithm A",
            "Algorithm B",
        ],
        "correct": 1,
        "explanation": "Using algorithm A's output, to choose an action we need argmax_a sum_{s'} p(s'|s,a)[r + γ v*(s')], which requires knowing transition probabilities p(s'|s,a). Algorithm B gives q*(s,a), allowing optimal action selection simply via argmax_a q*(s,a) without needing transition probabilities.",
    },
    {
        "question": "In proving that L_π is a contraction, we had the expression\nγ sum_j p(j|s)[v(j) - u(j)] ≤ γ ||v - u|| sum_j p(j|s)\nThis inequality holds because",
        "options": [
            "v(j) - u(j) is a component of ||v - u||",
            "the max norm of the difference on the LHS is less than the max norm of the difference on the RHS",
            "the expression on the LHS can take negative values, while the expression on the RHS will always be non-negative",
            "the max norm of the difference vector on the RHS will, at worst, be equal to the difference in components on the LHS",
        ],
        "correct": 3,
        "explanation": "The maximum norm ||v - u|| = max_j |v(j) - u(j)| will at worst be equal to the difference for any individual component j. Thus each term v(j) - u(j) is bounded by ||v - u||.",
    },
    {
        "question": "We defined the operator L_π : V -> V as L_π v = r_π + γ P_π v. Having seen the proof of the Banach fixed point theorem and assuming that vπ and v* have their usual meanings, which among the following are implications of showing that L_π is a contraction?",
        "options": [
            "vπ is a fixed point of L_π",
            "vπ is a unique fixed point of L_π",
            "repeatedly applying L_π on any value function v will result in convergence to vπ",
            "repeatedly applying L_π on any value function v will result in convergence to v*",
        ],
        "correct": [1, 2],
        "explanation": "Since L_π is a contraction, the Banach fixed point theorem guarantees the existence of a unique fixed point (b), and that repeated application of the contraction operator on any element in the metric space converges to that unique fixed point (c).",
    },
    {
        "question": "Given a value v ∈ V, suppose L_π v = v'. Then we can conclude that",
        "options": [
            "v = v'",
            "v ≠ v'",
            "||L_π v - L_π v'|| ≤ λ ||v - v'||, 0 ≤ λ < 1",
            "none of the above",
        ],
        "correct": 2,
        "explanation": "The first option may not hold if v ≠ v*. Similarly, the second option may not hold if v = v*. The third option must hold since L_π is a contraction mapping.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 5 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W5_2026 = [
    {
        "question": "In policy iteration, which of the following is/are true of the Policy Evaluation (PE) and Policy Improvement (PI) steps?",
        "options": [
            "The values of states that are returned by PE may fluctuate between high and low values as the algorithm runs.",
            "PE returns the fixed point of L_{πn}.",
            "PI can randomly select any greedy policy for a given value function vn.",
            "Policy iteration always converges for a finite MDP.",
        ],
        "correct": [1, 3],
        "explanation": "At each iteration, the PE step always returns values that are greater than or equal to the\nvalues of states from the previous iteration. So there is no fluctuation between high, and low\nvalues.\nSince the PE step always returns values that are greater than or equal to the values of states\nfrom the previous iteration, by breaking ties consistently when greedily selecting policies in\nthe PI stage, the policy returned by the PI step is always better than or equal to the policy\nfrom the previous iteration. Since for a finite MDP there are a finite number of deterministic\npolicies to search through, policy iteration must converge eventually.\n(b) is True. (c) is False - we need to break ties between policies consistently to guarantee\nthat the stopping criterion is met. (Refer to lectures).",
    },
    {
        "question": "Consider Monte-Carlo approach for policy evaluation. Suppose the states are S₁, S₂, S₃, S₄, S₅, S₆ and a terminal state. You sample one trajectory as follows:\nS₁ → S₅ → S₄ → S₆ → terminal state.\nWhich among the following states can be updated from this sample?",
        "options": [
            "S₁",
            "S₂",
            "S₆",
            "S₄",
        ],
        "correct": [0, 2, 3],
        "explanation": "Values of all states that appear in the trajectory can be updated.",
    },
    {
        "question": "Which of the following statements are true with regards to Monte Carlo value approximation\nmethods?",
        "options": [
            "To evaluate a policy using these methods, a subset of trajectories in which all states are\nencountered at least once are enough to update all state-values.",
            "Monte-Carlo value function approximation methods need knowledge of the full model.",
            "Monte-Carlo methods update state-value estimates only at the end of an episode.",
            "All of the above.",
        ],
        "correct": [0, 2],
        "explanation": "(a) State values of all states that appear in a trajectory can be updated simultaneously. So as\nlong as all states appears in at least one trajectory, we can make sure that all state-values for\nall states are updated. (c) Self-explanatory. (b) is wrong since these methods only require a\nway to sample trajectories from the environment.",
    },
    {
        "question": "In every visit Monte Carlo methods, multiple samples for one state are obtained from a single\ntrajectory. Which of the following is true?",
        "options": [
            "There is an increase in bias of the estimates.",
            "There is an increase in variance of the estimates.",
            "It does not affect the bias or variance of estimates.",
            "Both bias and variance of the estimates increase.",
        ],
        "correct": 0,
        "explanation": "Itonlyleadstoanincreaseinthebiasduetosometransitionsintheobtainedtrajectorybeing\nused multiple times, the distribution itself gets modified due to this.",
    },
    {
        "question": "Which of the following statements are FALSE about solving MDPs using dynamic program-\nming?",
        "options": [
            "If the state space is large or computation power is limited, it is preferred to update only\nsome states through random sampling or selecting states seen in trajectories.",
            "Knowledge of transition probabilities is not necessary for solving MDPs using dynamic\nprogramming.",
            "Methods that update only a subset of states at a time guarantee performance equal to or\nbetter than classic DP.",
            "None of the above.",
        ],
        "correct": [1, 2],
        "explanation": "(a) Valid reason for updating only subset of states at a time. (b) Solving MDPs using DP re-\nquiresknowledgeofthefullmodel,includingtransitionprobabilities. (c)Thereisnoguarantee\nthat it will be better than classic DP.",
    },
    {
        "question": "Select the correct statements about Generalized Policy Iteration (GPI).",
        "options": [
            "GPI lets policy evaluation and policy improvement interact with each other regardless of the details of the two processes.",
            "Before convergence, the policy evaluation step will usually cause the policy to no longer be greedy with respect to the updated value function.",
            "GPI converges only when a policy has been found which is greedy with respect to its own value function.",
            "The policy and value function found by GPI at convergence will both be optimal.",
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "Refer to Generalized Policy Iteration lectures.",
    },
    {
        "question": "What is meant by ”off-policy” Monte Carlo value function evaluation?",
        "options": [
            "The policy being evaluated is the same as the policy used to generate samples.",
            "The policy being evaluated is different from the policy used to generate samples.",
            "The policy being learnt is different from the policy used to generate samples.",
            "The policy being learnt is different from the policy used to generate samples.",
        ],
        "correct": 1,
        "explanation": "Monte Carlo value function evaluation is for valuation of a policy, not for learning one. ”Off-\npolicy”indicatesthatthesamplegeneratingpolicyisdifferentfromthepolicybeingevaluated.",
    },
    {
        "question": "For both value and policy iteration algorithms we will get a sequence of vectors after some\niterations, say v₁, v₂, ..., vₙ for value iteration and v′,v′...v′ for policy iteration. Which of the\n₁', v₂', ..., vₙ' for policy iteration. Which of the following statements are true?",
        "options": [
            "For all vᵢ ∈ {v₁, v₂, ..., vₙ} there exists a policy for which vᵢ is a fixed point.",
            "For all v′ ∈v′,v′....v′ there exists a policy for which v′ is a fixed point.\ni 1 2 n i",
            "For all vᵢ ∈ {v₁, v₂, ..., vₙ} there may not exist a policy for which vᵢ is a fixed point.",
            "For all v′ ∈v′,v′....v′ there may not exist a policy for which v′ is a fixed point.\ni 1 2 n i",
        ],
        "correct": [1, 2],
        "explanation": "The vectors in value iteration may not correspond to a policy but the vectors in policy iteration always correspond to some policy.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 5 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W5_2025 = [
    {
        "question": "For a particular finite MDP with bounded rewards, let V be the space of bounded functions\non S, the state space of the MDP. Let Π be the set of all policies, and let v be the value\nπ\nfunction corresponding to policy π where π ∈Π. Is it true that v ∈V, ∀π ∈Π?\nπ",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "The question essentially asks whether V contains all value functions, which we have seen in\nthe lectures to be true.",
    },
    {
        "question": "In the proof of the value iteration theorem, we saw that Lvₙ₊₁ = L_{πₙ₊₁} vₙ₊₁. Is it true, in general, that for an arbitrary bounded function v, Lv = L_π v (disregarding any special conditions that may be existing in the aforementioned proof)?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "",
    },
    {
        "question": "Continuing with the previous question, why is it the case that Lvₙ₊₁ = L_{πₙ₊₁} vₙ₊₁ in the proof of the value iteration theorem?",
        "options": [
            "because the equality holds in general",
            "because vn+1 is the optimal value function",
            "because we are considering only deterministic policies choosing a max valued action in\neach state",
            "because vn+1 is not a value function",
        ],
        "correct": 2,
        "explanation": "",
    },
    {
        "question": "Given that q (s,a)>v (s), we can conclude\nπ π",
        "options": [
            "action a is the best action that can be taken in state s",
            "π may be an optimal policy",
            "π is not an optimal policy",
            "none of the above",
        ],
        "correct": 2,
        "explanation": "Theinequalityindicatesthatthereexistsanactionthatiftakeninstates,theexpectedreturn\nwould be higher than the expected return of taking actions in state s as per policy π. While\nthisindicatesthatπ isnotanoptimalpolicy,itdoesnotindicatethataisthebestactionthat\ncan be taken in state s, since there may exist another action a(cid:48) such that q (s,a(cid:48))>q (s,a).\nπ π",
    },
    {
        "question": "Recall the problem described in the first question of the previous assignment. Use the MDP\nformulation arrived at in that question and starting with policy π(laughing) = π(silent) =\n(incense, no organ), perform a couple of policy iterations or value iterations (by hand!) until\nyou find an optimal policy (if you are taking a lot of iterations, stop and reconsider your\nformulation!). What are the resulting optimal state-action values for all state-action pairs?",
        "options": [
            "q (s,a)=8, ∀a\n∗",
            "q (s,a)=10, ∀a\n∗",
            "q (s,a∗)=10, q (s,a)=−10, ∀a(cid:54)=a∗\n∗ ∗",
            "q (s,a∗)=10, q (s,a)=8, ∀a(cid:54)=a∗\n∗ ∗",
        ],
        "correct": 3,
        "explanation": "First consider policy iteration.\nInitialisation: V(L)=V(Q)=0; π(L)=π(Q)=¬O∧I\nAssuming θ =0.7 and given, γ =0.9\nEvaluation:\n∆=0\nV(L)=Pπ(L)∗[Rπ(L)+γV(L)]+Pπ(L)∗[Rπ(L)+γV(Q)]=1∗(−1+0.9∗0)+0=−1\nLL LL LQ LQ\nV(Q)=Pπ(Q)∗[Rπ(Q)+γV(L)]+Pπ(Q)∗[Rπ(Q)+γV(Q)]=0+1∗(1+0.9∗0)=+1\nQL QL QQ QQ\n∆=1\nV(L)=Pπ(L)∗[Rπ(L)+γV(L)]+Pπ(L)∗[Rπ(L)+γV(Q)]=−1.9\nLL LL LQ LQ\nV(Q)=Pπ(Q)∗[Rπ(Q)+γV(L)]+Pπ(Q)∗[Rπ(Q)+γV(Q)]=+1.9\nQL QL QQ QQ\n∆=0.9\nV(L)=Pπ(L)∗[Rπ(L)+γV(L)]+Pπ(L)∗[Rπ(L)+γV(Q)]=−2.71\nLL LL LQ LQ\nV(Q)=Pπ(Q)∗[Rπ(Q)+γV(L)]+Pπ(Q)∗[Rπ(Q)+γV(Q)]=+2.71\nQL QL QQ QQ\n∆=0.81\nV(L)=Pπ(L)∗[Rπ(L)+γV(L)]+Pπ(L)∗[Rπ(L)+γV(Q)]=−3.439\nLL LL LQ LQ\nV(Q)=Pπ(Q)∗[Rπ(Q)+γV(L)]+Pπ(Q)∗[Rπ(Q)+γV(Q)]=+3.439\nQL QL QQ QQ\n∆=0.729\nV(L)=Pπ(L)∗[Rπ(L)+γV(L)]+Pπ(L)∗[Rπ(L)+γV(Q)]=−4.0951\nLL LL LQ LQ\nV(Q)=Pπ(Q)∗[Rπ(Q)+γV(L)]+Pπ(Q)∗[Rπ(Q)+γV(Q)]=+4.0951\nQL QL QQ QQ\n∆=0.6561\nImprovement:\nπ(L)=O∧I (or O∧¬I)\nπ(Q)=¬O∧I\nEvaluation:\n∆=0\nV(L)=Pπ(L)∗[Rπ(L)+γV(L)]+Pπ(L)∗[Rπ(L)+γV(Q)]=+4.6856\nLL LL LQ LQ\n2\n\nV(Q)=Pπ(Q)∗[Rπ(Q)+γV(L)]+Pπ(Q)∗[Rπ(Q)+γV(Q)]=+4.6856\nQL QL QQ QQ\n∆=0.5905\nImprovement:\nπ(L)=O∧I (or O∧¬I)\nπ(Q)=¬O∧I\nNo change in policy. This is an optimal policy.\nNow consider value iteration.\nInitialisation: V(L)=V(Q)=0; Assuming θ =0.9\n∆=0\nV(L)=max {Pa ∗[Ra +γV(L)]+Pa ∗[Ra +γV(Q)]}\na LL LL LQ LQ\nFor a=O∧I or O∧¬I:\nV(L)=+1\nV(Q)=max {Pa ∗[Ra +γV(L)]+Pa ∗[Ra +γV(Q)]}\na QL QL QQ QQ\nFor a=¬O∧I: V(Q)=+1\n∆=1\nV(L)=+1.9 for a=O∧I or O∧¬I\nV(Q)=+1.9 for a=¬O∧I\n∆=0.9\nV(L)=+2.71 for a=O∧I or O∧¬I\nV(Q)=+2.71 for a=¬O∧I\n∆=0.81\nDeterministic policy:\nπ(L)=O∧I (or O∧¬I)\nπ(Q)=¬O∧I\nContinuingevaluationwillleadtoconvergencevaluesof±10(±1(1+γ+γ2+...)= ±1 = ±1).\n1−γ .1\nOptimal state-action values:\nCurrent state Action Next state q (s,a)\n(cid:63)\nL O∧I Q +10\nL O∧¬I Q +10\nL ¬O∧I L +8\nL ¬O∧¬I L +8\nQ O∧I L +8\nQ O∧¬I L +8\nQ ¬O∧I Q +10\nQ ¬O∧¬I L +8\nNote: q (s,a)=+10whenanoptimalactionistakeninanystate,whereas+8(=−1+0.9∗10)\n(cid:63)\nresultswhenaninitialsub-optimalactionisfollowedbyactionstakenaccordingtoanoptimal\npolicy.",
    },
    {
        "question": "In the previous question, what does the state value function converge to for the policy we\nstarted off with?",
        "options": [
            "v (laughing)=v (silent)=10\nπ π",
            "v (laughing)=8, v (silent)=10\nπ π",
            "v (laughing)=−10, v (silent)=10\nπ π",
            "v (laughing)=−8, v (silent)=10\nπ π",
        ],
        "correct": 2,
        "explanation": "Refer to the solution of the previous question.",
    },
    {
        "question": "In solving an episodic problem we observe that all trajectories from the start state to the goal\nstate pass through a particular state exactly twice. In such a scenario, is it preferable to use\nfirst-visit or every-visit MC for evaluating the policy?",
        "options": [
            "first-visit MC",
            "every-visit MC",
            "every-visit MC with exploring starts",
            "neither, as there are issues with the problem itself",
        ],
        "correct": 3,
        "explanation": "A state having to be visited exactly twice in any trajectory from the start state to the goal\nstate indicates that the problem environment does not follow the Markov property.",
    },
    {
        "question": "Which of the following are advantages of Monte Carlo methods over dynamic programming\ntechniques?",
        "options": [
            "the ability to learn from actual experience",
            "the ability to learn from simulated experience",
            "the ability to estimate the value of a single state independent of the number of states",
            "the ability to show guaranteed convergence to an optimal policy",
        ],
        "correct": [0, 1, 2],
        "explanation": "Option (c) is an advantage, since it allows us to estimate values of only specific states of an\nMDP if those are the only states we care to know about.",
    },
    {
        "question": "For a specific MDP, suppose we have a policy that we want to evaluate through the use of\nactual experience in the environment alone and using Monte Carlo methods. Wedecidetouse\nthe first-visit approach along with the technique of always picking the start state at random\nfrom the available set of states. Will this approach ensure complete evaluation of the action\nvalue function corresponding to the policy?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "Dependinguponthepolicy,startingfromrandomstatesalonewillnotensureobservingreturns\nfor each state-action pairs, which is required to fully evaluate q .\nπ",
    },
    {
        "question": "Assuming an MDP where there are n actions a ∈ A each of which is applicable in each state\ns∈S, if π is an ϵ-soft policy for some ϵ>0, then",
        "options": [
            "π(a|s)=ϵ, ∀a,s",
            "π(a|s)= ϵ, ∀a,s\nn",
            "π(a|s)>= ϵ, ∀a,s\nn",
            "π(a(cid:48)|s)=1−ϵ+ ϵ, π(a|s)= ϵ, ∀a(cid:54)=a(cid:48), ∀s\nn n",
        ],
        "correct": 2,
        "explanation": "An ϵ-soft policy is one where the probability of selecting any action is at least ϵ/n.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 6 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W6_2026 = [
    {
        "question": "Assertion: In order to use importance sampling for off-policy Monte-Carlo policy evaluation, we require knowledge of the state transition probabilities of the MDP.\nReason: We require knowledge of the probability of each trajectory xᵢ according to the estimation policy and according to the behaviour policy. Both of these values are dependent on the state transition probabilities of the MDP.",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true, Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 3,
        "explanation": "The importance factor only depends on the ratio between the probability of each trajectory xᵢ according to the estimation policy and according to the behaviour policy. The state transition probabilities cancel out in this ratio. Consequently, we do not require knowledge of the state-transition probabilities for off-policy Monte-Carlo policy evaluation.",
    },
    {
        "question": "Which of the following are true?",
        "options": [
            "Dynamic programming methods use full backups and bootstrapping.",
            "Temporal-Difference methods use sample backups and bootstrapping.",
            "Monte-Carlo methods use sample backups and bootstrapping.",
            "Monte-Carlo methods use full backups and no bootstrapping.",
        ],
        "correct": [0, 1],
        "explanation": "Refer to the lecture on TD(0).",
    },
    {
        "question": "Which of the following statement(s) is/are true for the UC-Trees algorithm?",
        "options": [
            "We typically require a simulation model for the environment.",
            "It uses ϵ-greedy exploration for action selection.",
            "It computes an upper confidence bound on the value of (state, action) pairs.",
            "It is a variation of the Monte-Carlo tree search algorithm.",
        ],
        "correct": [0, 2, 3],
        "explanation": "Refer to the lecture on UC-Trees.",
    },
    {
        "question": "Consider the following statements:\n(i) TD(0) methods use an unbiased sample of the return.\n(ii) TD(0) methods use a sample of the reward from the distribution of rewards.\n(iii) TD(0) methods use the current estimate of value function.\nWhich of the above statements is/are true?",
        "options": [
            "(i), (ii)",
            "(i),(iii)",
            "(ii), (iii)",
            "(i), (ii), (iii)",
        ],
        "correct": 2,
        "explanation": "Refer the lecture on TD(0).",
    },
    {
        "question": "Assertion: Q-learning can use asynchronous samples from different policies to update Q\nvalues.\nReason: Q-learning is an off-policy learning algorithm.",
        "options": [
            "Assertion and Reason are both true and Reason is a correct explanation of Assertion.",
            "Assertion and Reason are both true and Reason is not a correct explanation of Assertion.",
            "Assertion is true but Reason is false.",
            "Assertion is false but Reason is true.",
        ],
        "correct": 0,
        "explanation": "The learned action-value function directly approximates the optimal action-value function independent of the policy being followed.",
    },
    {
        "question": "Suppose, for a 2 player game that we have modeled as an MDP, instead of learning a policy\nover the MDP directly, we separate the deterministic and stochastic result of playing an action to create ‘after-states’ (as discussed in the lectures). Consider the following statements:\n(i) The set of states that make up ‘after-states’ may be different from the original set of\nstates for the MDP.\n(ii) The set of ‘after-states’ could be smaller than the original set of states for the MDP.\nWhich of the above statements is/are True?",
        "options": [
            "Only (i)",
            "Only (ii)",
            "Both (i) and (ii)",
            "Neither (i) nor (ii).",
        ],
        "correct": 2,
        "explanation": "In tic-tac-toe for example, if the agent plays first, then the original set of states will all have\nan even number of marks (knot/cross) on the board. All after-states on the other hand, will\nall have an odd number of marks on the board. Hence (i) is True.\nAs discussed in the lectures, several of the original states of the MDP could map to the same\nafter-state (once an action is played), so (ii) is True.",
    },
    {
        "question": "Consider the environment given below (CliffWorld discussed in lecture):\nSuppose we use ϵ-greedy policy for exploration with a value of ϵ = 0.1. Select the correct option(s):",
        "options": [
            "Q-Learning finds the optimal (red) path.",
            "Q-Learning finds the safer (blue) path.",
            "SARSA finds the optimal (red) path.",
            "SARSA finds the safer (blue) path.",
        ],
        "correct": [0, 3],
        "explanation": "Q-Learning being off-policy finds the estimates for the optimal policy whereas SARSA being\non-policy, finds a safer path due to -100 reward of falling in the cliff during exploration.",
    },
    {
        "question": "Assertion: Having a simulator/model is an advantage when using rollouts based methods.\nReason: Multiple trajectories can be sampled from the model from any given state.",
        "options": [
            "Assertion and Reason are both true and Reason is a correct explanation of Assertion.",
            "Assertion and Reason are both true and Reason is not a correct explanation of Assertion.",
            "Assertion is true but Reason is false.",
            "Assertion and Reason are both false.",
        ],
        "correct": 0,
        "explanation": "Having a model is necessary when using rollouts based methods. If a simulator is not present,\nthe state from which multiple trajectories are being created needs to be reached multiple times, and multiple trajectories will actually need to be ”played”. In comparison, simulating trajectories\nin a model that is present, without actually having to ”play” them in the environment is\nsignificantly better.",
    },
    {
        "question": "Consider an MDP with two states A and B. Given the single trajectory shown below (in the\npattern of state, reward, next state...), use on-policy TD(0) updates to make estimates for the\nvalues of the 2 states.\nA,3,B,2,A,5,B,2,A,4,END\nAssume a discount factor γ =1, a learning rate α=1 and initial state-values of zero. What\nare the estimated values for the 2 states at the end of the sampled trajectory? (Note: You are\nnot asked to compute the true values for the two states.)",
        "options": [
            "V(A)=2,V(B)=10",
            "V(A)=8,V(B)=7",
            "V(A)=4,V(B)=12",
            "V(A)=12,V(B)=7",
        ],
        "correct": 2,
        "explanation": "The TD(0) update rule is: V (s )=V (s )+α[R +γV (s )−V (s )]\nnew t old t t+1 old t+1 old t\nGiven the parameters γ =1, and α=1, this rule simply becomes:\nV (s )=R +V (s )\nnew t t+1 old t+1\nStarting with state-values of zero and making updates along the sampled trajectory, we have\nthe following updates:\nV(A)= 3 + V(B) = 3\nV(B)= 2 + V(A) = 5\nV(A)= 5 + V(B) = 10\nV(B)= 2 + V(A) = 12\nV(A)= 4\nSo, at the end of the trajectory, we have estimates: V(A)=4, V(B)=12",
    },
    {
        "question": "Which one of the following statements are True for SARSA?",
        "options": [
            "It uses bootstrapping to approximate full return.",
            "It is an on-policy algorithm.",
            "It is a TD method.",
            "It always selects the greedy action choice.",
        ],
        "correct": [0, 1, 2],
        "explanation": "(d) is false. SARSA requires adequate exploration of the state space to converge to an optimal policy.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 6 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W6_2025 = [
    {
        "question": "In the search procedure listed in the lecture for Monte-Carlo tree search what is/are the uses\nof the depth parameter?",
        "options": [
            "allows us to identify leaf states",
            "allows us to identify terminal states",
            "can be used to impact the choice of action selection",
            "allows us to specialise value functions based on the number of steps that have been taken",
        ],
        "correct": [0, 2, 3],
        "explanation": "",
    },
    {
        "question": "Suppose you are given a finite set of transition data. Assuming that the Markov model that\ncan be formed with the given data is the actual MDP from which the data is generated, will\nthe value functions calculated by the MC and TD methods (in a manner similar to what we\nsaw in the lectures) necessarily agree?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "Inourlectureexample,wesawthatthevaluefunctionscalculatedbytheMCandTDmethods\ndid not agree. The same would still hold if the MDP that generated the data was the MDP\nthat we formed from the data in applying the TD method.",
    },
    {
        "question": "In the iterative policy evaluation process, we have seen the use of different update equations\nin DP, MC, and TD methods. With regard to these update equations",
        "options": [
            "DP and TD make use of estimates but not MC",
            "TD makes use of estimates but not DP and MC",
            "MC and TD make use of estimates but not DP",
            "all three methods make use of estimates",
        ],
        "correct": 3,
        "explanation": "DP methods update estimates based on other learned estimates, i.e., they bootstrap. MC\nmethods, while they do not bootstrap, make use of estimates because the target in MC meth-\nods, i.e., the sample return, is an estimate of the actual expected return; the expected value\nofcourse, isnotknown. TDmethodsuseboththeabove, i.e., theymakeuseofsamplesofthe\nexpected values as well as bootstrap.",
    },
    {
        "question": "Is it necessary for the behaviour policy of an off-policy learning method to have non-zero\nprobability of selecting all actions?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "If the probability of selecting certain actions in the estimation policy, i.e., the policy which\nis being evaluated and/or improved, is zero, then the corresponding probability of selecting\nthose same actions in the behaviour policy can also be zero without causing any problem to\nthe off-policy learning procedure.",
    },
    {
        "question": "With respect to the Expected SARSA algorithm, is exploration (using for example ϵ-greedy\naction selection) required as it is in the normal SARSA and Q-learning algorithms?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "The difference in the update rules that differentiate Expected SARSA from the SARSA al-\ngorithm do not obviate the need for exploration in the former, since without exploration the\nalgorithm would, in general, miss out on large parts of the state space, preventing it from\ncorrectly converging (in the limit) to an optimal policy.",
    },
    {
        "question": "Assume that we have available a simulation model for a particular problem. To learn an optimal policy, instead of following trajectories end-to-end, in each iteration we randomly supply a state and an action to the model and receive the corresponding reward. This information is used for updating the value function. Which method among the following would you expect to work\nin this scenario?",
        "options": [
            "SARSA",
            "Expected SARSA",
            "Q-learning",
            "none of the above",
        ],
        "correct": 3,
        "explanation": "Notethateachofthethreealgorithmslistedaboverequire,inadditiontothereward,thenext\nstate information, which is not provided by the described simulation model.",
    },
    {
        "question": "Consider the following transitions observed for an undiscounted MDP with two states P and\nQ.\nP, +3, P, +2, Q, -4, P, +4, Q, -3\nQ, -2, P, +3, Q, -3\nEstimates the state value function using first-visit Monte-Carlo evaluation.",
        "options": [
            "v(P) = 2, v(Q) = -5/2",
            "v(P) = 2, v(Q) = 0",
            "v(P) = 1, v(Q) = -5/2",
            "v(P) = 1, v(Q) = 0",
        ],
        "correct": 2,
        "explanation": "Forfirst-visitMC,we consideronlythefirst occurrence ofeachstate ineachtransition. Thus,\nwe have\nv(P) = (2 + 0)/2 = 1\nv(Q) = (-3 - 2)/2 = -5/2",
    },
    {
        "question": "Considering the same transition data as above, estimate the state value function using the\nevery-visit Monte-Carlo evaluation.",
        "options": [
            "v(P) = 2, v(Q) = -5/2",
            "v(P) = 2, v(Q) = -11/4",
            "v(P) = 1/2, v(Q) = -11/4",
            "v(P) = 1/4, v(Q) = -5/2",
        ],
        "correct": 2,
        "explanation": "In the every-visit case we consider each occurrence of each state in the transitions. Thus, we\nhave\nv(P) = (2 + -1 + 1 + 0)/4 = 1/2\nv(Q) = (-3 - 3 - 2 - 3)/4 = -11/4",
    },
    {
        "question": "Construct a Markov model that best explains the observations given in question 7. In this\nmodel, what is the probability of transitioning from state P to itself? What is the expected\nreward received on transitioning from state Q to state P?",
        "options": [
            "1/4, -4",
            "1/4, -3",
            "1/2, -4",
            "1/2, -3",
        ],
        "correct": 1,
        "explanation": "Following is the model that can be constructed from the available data.",
    },
    {
        "question": "What would be the value function estimate if batch TD(0) were applied to the above transac-\ntion data?",
        "options": [
            "1, -1/2",
            "1, -2",
            "2, -1/2",
            "2, -2",
        ],
        "correct": 3,
        "explanation": "We can solve the Bellman equations directly based on the above model to get\nv(A) = 3 + 1/4 * v(A) + 3/4 * v(B)\nv(B) = -3 + 1/2 * v(A)\nv(A) = 2\nv(B) = -2",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 7 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W7_2026 = [
    {
        "question": "Which of the following is the corrected n-step truncated return?",
        "options": [
            "R_{t+n} + γⁿ V_t(s_{t+n})",
            "R_{t+1} + γ R_{t+2} + γ² R_{t+3} + ... + γⁿ⁻¹ R_{t+n} + γⁿ V_t(s_{t+n})",
            "γ R_{t+1} + γ² R_{t+2} + γ³ R_{t+3} + ... + γⁿ R_{t+n} + V_t(s_{t+n})",
            "None of the above.",
        ],
        "correct": 1,
        "explanation": "From the definition of G_t^{(n)} given in ”Eligibility Traces” video.",
    },
    {
        "question": "Which of the following is correct way to implement replacing traces?",
        "options": [
            "E_t(s) = 1 if s_t ≠ s, else (γλ)E_{t-1}(s)",
            "E_t(s) = (γλ)E_{t-1}(s) + 1 if s_t = s, else (γλ)E_{t-1}(s)",
            "E_t(s) = (γλ)E_{t-1}(s) + 1 if s_t ≠ s, else (γλ)E_{t-1}(s)",
            "E_t(s) = 1 if s_t = s, else (γλ)E_{t-1}(s)",
        ],
        "correct": 3,
        "explanation": "(d) correctly defines replacing traces: setting the trace to 1 upon visiting state s, and decaying by γλ otherwise.",
    },
    {
        "question": "Assertion: TD(1), a way of implementing Monte Carlo with eligibility traces, extends Monte Carlo algorithm for continuing tasks.\nReason: TD(1), implemented with eligibility traces, is an offline algorithm.",
        "options": [
            "Assertion and Reason are both true and Reason is a correct explanation of Assertion",
            "Assertion and Reason are both true and Reason is not a correct explanation of Assertion",
            "Assertion is true and Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 2,
        "explanation": "TD(λ) with λ=1 gives the Monte Carlo return as its target and hence TD(1) extends Monte Carlo for online implementation for continuing tasks. TD(1) however is an online algorithm with eligibility traces.",
    },
    {
        "question": "Assertion: It is NOT necessary for behavior policy of an off-policy method to have non-zero probability of selecting all actions.\nReason: If probability of certain actions in estimation policy is zero, then probability of selecting corresponding actions in behavior policy can be zero, and it would not cause trouble in learning procedure.",
        "options": [
            "Assertion and Reason are both true and Reason is a correct explanation of Assertion.",
            "Assertion and Reason are both true and Reason is not a correct explanation of Assertion.",
            "Assertion is true but Reason is false.",
            "Assertion and Reason are both false.",
        ],
        "correct": 0,
        "explanation": "actions for which probability in both policies is zero can simply be ignored and thus, there can be actions having zero probability in a policy. So both statements are true and reason is correct explanation for assertion.",
    },
    {
        "question": "Considering episodic tasks and for λ ∈ (0,1), one-step return always gets assigned the maximum weight in the λ-return. True or false.",
        "options": [
            "False",
            "True",
        ],
        "correct": 0,
        "explanation": "It depends on the length of an episode (as well as the value of λ). For example, consider an episode of length 3 and a value of λ=0.7.",
    },
    {
        "question": "Assertion: It is possible to use the forward view of eligibility traces based target for updates before the end of an episode.\nReason: G_t^λ is the weighed average of terms of the form G_t^i, where each G_t^i is computable after a finite number of steps i, making G_t^λ also computable after a finite number of steps in all cases.",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true, Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 3,
        "explanation": "The assertion is wrong, the forward view of eligibility traces based target cannot be computed till the end of the episode, making updates before the end of an episode impossible. The reason is wrong as well, each G_t^i is computable after i steps, however i has no upper bound, making G_t^λ impossible to calculate in a finite amount of time in some cases.",
    },
    {
        "question": "Which of the following is a way to use replacing traces in SARSA(λ) such that we only update the estimate for the action, a, taken in the state, s, in a trajectory at timestep t?",
        "options": [
            "E_t(s,a) = γλE_{t-1}(s,a) + 1 if s_t=s, a_t=a; else (γλ)E_{t-1}(s,a)",
            "E_t(s,a) = 1 if s_t=s, a_t=a; else (γλ)E_{t-1}(s,a)",
            "E_t(s,a) = γλE_{t-1}(s,a) + 1 if s_t=s, a_t=a; 0 if s_t=s, a_t≠a; else (γλ)E_{t-1}(s,a)",
            "E_t(s,a) = 1 if s_t=s, a_t=a; 0 if s_t=s, a_t≠a; else (γλ)E_{t-1}(s,a)",
        ],
        "correct": 3,
        "explanation": "(d) is an aggressive form of replacing traces update for SARSA(λ) where we update estimate only for estimate for action taken in a state by making traces for other actions zero.",
    },
    {
        "question": "Assertion: When using an ϵ-greedy exploration strategy, and Watkins Q(λ), the ϵ value must be kept low.\nReason: Traces will become too short if a high value of ϵ is used, negating many of the advantages of using eligibility traces.",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true, Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 0,
        "explanation": "Explained in the video ”Eligibility Trace Control” in minutes 21:00 to 24:30. Every time an exploratory action is taken, the trace ends, causing traces to become too short.",
    },
    {
        "question": "Consider the current state is s and the action recommended by the policy, a_1, is taken. The possible reason(s) behind setting ∀a≠a_1, E_t(s,a)=0, is/are:\n(i) Rewards obtained by taking a_1 in s should not be attributed to actions other than a_1 taken when in state s previously.\n(ii) It assumed that the timesteps between reaching s are large enough to decay the eligibility trace to 0.\nWhich of the above is/are the correct reason(s)?",
        "options": [
            "Only (i)",
            "Only (ii)",
            "Both (i) and (ii)",
            "None of the above",
        ],
        "correct": 0,
        "explanation": "Explained in the video ”Eligibility Trace Control”. (i) is the correct reason.",
    },
    {
        "question": "In off-policy TD(λ), which of the following is a correct way to update eligibility trace, if π is the policy whose Q-values we want to estimate, µ is the behaviour policy, and ρ_t = π(s_t,a_t) / µ(s_t,a_t)?",
        "options": [
            "E_t(s) = ρ_t γλE_{t-1}(s) + 1 if s_t=s; else ρ_t γλE_{t-1}(s)",
            "E_t(s) = ρ_t (γλE_{t-1}(s) + 1) if s_t=s; else ρ_t γλE_{t-1}(s)",
            "E_t(s) = γλE_{t-1}(s) + 1 if s_t=s; else ρ_t γλE_{t-1}(s)",
            "E_t(s) = ρ_t (γλE_{t-1}(s) + 1) if s_t=s; else γλE_{t-1}(s)",
        ],
        "correct": 1,
        "explanation": "The correct equation for this update is (b) as it takes care of importance sampling ratio for both cases, s_t=s and otherwise, by multiplying ρ_t to both terms.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 7 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W7_2025 = [
    {
        "question": "Consider example 7.1 and figure 7.2 in the text book. Which among the following steps\n(keeping all other factors unchanged) will result in a decrease in the RMS errors shown in the\ngraphs?",
        "options": [
            "increasing the number of states of the MDP",
            "increasing the number of episodes over which error is calculated",
            "increasing the number of repetitions over which the error is calculated",
            "none of the above",
        ],
        "correct": 1,
        "explanation": "Note that the graphs are generated by averaging over the first 10 episodes. If we increase the\nnumber of episodes considered, the error shown in the graphs would reduce as evaluation of\nthe policy improves.",
    },
    {
        "question": "Considering episodic tasks and for λ ∈ (0,1), is it true that the one step return always gets\nassigned the maximum weight in the λ-return?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "This is not necessarily true and depends on the length of an episode (as well as the value of\nλ). For example, consider an episode of length 3 and a value of λ=0.7.",
    },
    {
        "question": "In the TD(λ) algorithm, if λ=1 and γ =1, then which among the following are true?",
        "options": [
            "the method behaves like a Monte Carlo method for an undiscounted task",
            "the eligibility traces do not decay",
            "the value of all states are updated by the TD error in each episode",
            "this method is not suitable for continuing tasks",
        ],
        "correct": [0, 1, 3],
        "explanation": "Note that even if λ = 1 and the eligibility traces do not decay, states must first be visited\nbefore their values can be updated.",
    },
    {
        "question": "Assume you have a MDP with |S| states. You decide to use an n-step truncated corrected\nreturn for the evaluation problem on this MDP. Do you think that there is any utility in\nconsidering values of n which exceed |S| for this problem?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "Note that the number of steps in an n-step truncated corrected return is related to the length\nof the trajectories which can exceed the number of states in the state space of a problem.",
    },
    {
        "question": "Which among the following are reasons to support your answer in the previous question?",
        "options": [
            "only values of n≤|S| should be considered as the number of states is only |S|",
            "all implementations with n > |S| will result in the same evaluation at each stage of the\niterative process",
            "the length of each episode may exceed |S|, and hence values of n>|S| should be consid-\nered",
            "regardless of the number of states, different values of n will always lead to different\nevaluations (at each step of the iterative process) and hence cannot be disregarded",
        ],
        "correct": 2,
        "explanation": "",
    },
    {
        "question": "Consider the text book figure 5.1 describing the first-visit MC method prediction algorithm\nand figure 7.7 describing the TD(λ) algorithm. Will these two algorithms behave identically\nfor λ=1? If so, what kind of eligibility trace will result in equivalence?",
        "options": [
            "no",
            "yes, accumulating traces",
            "yes, replacing traces",
            "yes, dutch traces, with α=0.5",
        ],
        "correct": 0,
        "explanation": "The two algorithms are not identical since figure 7.7 describes the online version of the TD(λ)\nalgorithm, whereas in the MC algorithm described in figure 5.1, updates are obviously not\nmade after each individual reward is observed.",
    },
    {
        "question": "Given the following sequence of states observed from the beginning of an episode,\ns ,s ,s ,s ,s ,s ,s ,s\n2 1 3 2 1 2 1 6\nwhat is the eligibility value, e (s ), of state s at time step 7 given trace decay parameter λ,\n7 1 1\ndiscount rate γ, and initial value, e (s )=0, when accumulating traces are used?\n0 1",
        "options": [
            "γ7λ7",
            "(γλ)7+(γλ)6+(γλ)3+γλ",
            "γλ(1+γ2λ2+γ5λ5)",
            "γ7λ7+γ3λ3+γλ",
        ],
        "correct": 2,
        "explanation": "According to the non-recursive expression for accumulating eligibility trace, we have\nt\n(cid:88)\ne (s)= (γλ)t−kI\nt ssk\nk=0\nwhere I is an indicator function.\nssk\nUsing the above expression along with the given state sequence, we have\ne (s )=(γλ)7−1+(γλ)7−4+(γλ)7−6 =γλ+γ3λ3+γ6λ6\n7 1",
    },
    {
        "question": "For the above question, what is the eligibility value if replacing traces are used?",
        "options": [
            "γ7λ7",
            "γλ",
            "γλ+1",
            "3γλ",
        ],
        "correct": 1,
        "explanation": "We know that when using replacing traces, the eligibility trace of a state is set to 1 if that\nstate is visited and decayed by a factor of γλ otherwise. Thus, the latest occurrence of state\ns just before state s would cause e (s ) to be set to 1 and after the occurrence of state s ,\n1 6 6 1 6\nthis would decay to e (s )=γλ.\n7 1",
    },
    {
        "question": "In solving the control problem, suppose that at the start of an episode the first action that\nis taken is not an optimal action according to the current policy. Would an update be made\ncorresponding to this action and the subsequent reward received in Watkin’s Q(λ) algorithm?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "This is immediately clear from the Watkin’s Q(λ) algorithm described in the text.",
    },
    {
        "question": "Suppose that in a particular problem, the agent keeps going back to the same state in a loop.\nWhat is the maximum value that can be taken by the eligibility trace of such a state if we\nconsider accumulating traces with λ=0.25 and γ =0.8?",
        "options": [
            "1.25",
            "5.0",
            "∞",
            "insufficient data",
        ],
        "correct": 0,
        "explanation": "Foraccumulating tracesmaximum increaseineligibilityoccursifthe stateis selected: e (s)=\nt\nγλe (s)+1. At maximum, e (s)=e (s), giving, e (s)=e (s)= 1 .\nt−1 t t−1 t t−1 1−γλ",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 8 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W8_2026 = [
    {
        "question": "You are given a training set of vectors Φ, so that each row of the matrix Φ corresponds to k\nattributesofasingletrainingsample. Supposethatyouareaskedtofindalinearfunctionthat\nminimizesthemeansquarederrorforagivensetofstationarytargetsy usinglinearregression.\nState true/false for the following statement.\nStatement: If the column vectors of Φ are linearly independent, then there exists a unique\nlinear function that minimizes the mean-squared-error.",
        "options": [
            "True",
            "False",
        ],
        "correct": 0,
        "explanation": "IfthecolumnvectorsofΦarelinearlyindependent,then(ΦTΦ)isinvertible. Usingtheclosed\nformsolutionθ =(ΦTΦ)−1 ΦTy, auniquesolutiontothelinearregressionproblemmustexist.",
    },
    {
        "question": "Which of the following statements are true ?",
        "options": [
            "Function approximation allows us to deal with continuous state spaces.",
            "A lookup table is a linear function approximator.",
            "State aggregates do not overlap in coarse-coding.",
            "None of the above.",
        ],
        "correct": [0, 1],
        "explanation": "Refer to the lectures on function approximation.",
    },
    {
        "question": "In which of the following cases, the loss of a function appoximator as (cid:80) (Vˆ(s)−V(s))2\ns∈S\nwould lead to poor performance? Consider ’relevant’ states to be those which are visited\nfrequently when executing near optimal policies.",
        "options": [
            "Large state space with small percentage of relevant states.",
            "Small state space with large percentage of relevant states.",
            "Large state space with large percentage of relevant states.",
            "None of the above.",
        ],
        "correct": 0,
        "explanation": "A small percentage of relevant states would cause poor performance in this case. Due to only\na few states being relevant, it would be more important for the function approximator to do\nwell in those states as compared to irrelevant states. However in the given loss function, all\nstates are equally important, which will make it perform poorly.",
    },
    {
        "question": "Assertion: It is not possible to use look-up table based methods to solve continuous state\nor action space problems. (Assume discretization of continuous space is not allowed)\nReason: Forcontinuousstateoractionspace,thereareaninfinitenumberofstates/actions.",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true, Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 0,
        "explanation": "Unless the space is split into discrete points, it is not possible to maintain a look up table.",
    },
    {
        "question": "Assertion: If we make incremental updates for a linear approximation of the value function\nvˆ under a policy π, using gradient descent to minimize the mean-square-error between vˆ(s )\nt\nandbootstrappedtargetsR +γvˆ(s ), thenwewilleventuallyconvergetothesamesolution\nt t+1\nthat we would have if we used the true v values as targets instead.\nπ\nReason: Each update moves vˆ closer to v , so eventually the bootstrapped targets R +\nπ t\nγvˆ(s ) will converge to the true v (s ) values\nt+1 π t\n(Assume that we sample on-policy)",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true and Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 3,
        "explanation": "On account of the non-stationarity of the bootstrapped targets, we cannot guarantee that\nwe will converge to the same solution (least-squares fit), however, assuming that the column\nvectors of the design matrix Φ are linearly independent, the distance between the function\nthat we converge to vˆ∗ and the least squares fit for the targets v (which is denoted by vˆopt in\nπ\nthe lectures) is bounded.",
    },
    {
        "question": "Assertion: To solve the given optimization problem for some states with linear function\napproximator,\nπ (s)=argmax Qˆπt(s,a)\nt+1\na\nin case of discrete action space, we need to formulate a classification problem.\nReason: The given problem is equivalent to solving:\nπ (s)=argmax Φ(s)⊤Θˆπt(a)\nt+1\na\nFor discrete action space, as we can’t maximize it explicitly, we need to formulate a classifica-\ntion problem.",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true, Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 3,
        "explanation": "Asitsdiscreteactionspace,wedonotneedtotrainaclassifier. Wecansimplypasstheactions\nthrough the function approximator and pick the one with maximum estimated Q-value.",
    },
    {
        "question": "Which of the following is/are true about the LSTD and LSTDQ algorithm?",
        "options": [
            "Both are iterative algorithms, where the estimate of the parameters are updated using\nthe gradient information of the loss function.",
            "Both LSTD and LSTDQ can reuse samples.",
            "Both LSTD and LSTDQ are linear function approximation methods.",
            "None of the above",
        ],
        "correct": 2,
        "explanation": "Refer to videos on LSTD and LSTDQ",
    },
    {
        "question": "Assertion: When minimizing mean-squared-error to approximate the value of states under\na given policy π, it is important that we draw samples on-policy.\nReason: Sampling on-policy makes the training data approximately reflect the steady state\ndistribution of states under the policy π.",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true and Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 0,
        "explanation": "Both the Assertion and Reason are true, and the Reason is a correct explanation for the\nAssertion. Refer to the lecture on function approximation.",
    },
    {
        "question": "Tile coding is a method of state aggregation for gridworld problems. Consider the following\nstatements.\n(i) The number of indicators for each state is equal to number of tilings.\n(ii) Tile coding cannot be used in continuous state spaces.\n(iii) Tile coding is also a form of Coarse coding.\nSay which of the above statements are true",
        "options": [
            "(iii) only",
            "(i), (iii)",
            "(i) only",
            "(i), (ii), (iii)",
        ],
        "correct": 1,
        "explanation": "Tilecodingisoneapproachofcoarsecodingforgrid-world. Also, thenumberoftilingscanbe\nanything as per requirement and number of indicators are equal to number of tilings.",
    },
    {
        "question": "Which of the following are the correct values for A˜ in LSTDQ method.\nNote the samples are D = {s ,a ,s′,r }, ϕ(s ,a ) is the representation used for (s ,a ) pair\ni i i i i i i i\nand π is the policy being followed.",
        "options": [
            "1 (cid:80)L [ϕ(s ,a )(ϕ(s ,a )−γϕ(s′,a ))T]\nL i=1 i i i i i i",
            "1 (cid:80)L [ϕ(s )(ϕ(s )−γϕ(s′))T]\nL i=1 i i i",
            "1 (cid:80)L [ϕ(s ,a )(ϕ(s ,a )−γϕ(s′))T]\nL i=1 i i i i i",
            "1 (cid:80)L [ϕ(s ,a )(ϕ(s ,a )−γϕ(s′,π(s′)))T]\nL i=1 i i i i i i",
        ],
        "correct": 3,
        "explanation": "Φ matrix contains features for each state action pair, and a policy π is followed. So when we\nare in state s′ the correct feature to use is ϕ(s′,π(s′)) since after reaching the state s′ in the\ni i i i\nfuture we would have taken the action π(s′). so 1 (cid:80)L [ϕ(s ,a )(ϕ(s ,a )−γϕ(s′,π(s′)))T]\ni L i=1 i i i i i i\nis the correct answer",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 8 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W8_2025 = [
    {
        "question": "Is the problem of non-stationary targets an issue when using Monte Carlo returns as targets?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "When Monte Carlo returns are used as targets, then the targets are stationary as the target\nvalues do not change as the parameters evolve.",
    },
    {
        "question": "Inaparameterisedrepresentationofthevaluefunction,weuseafeaturewhichactsasacounter\nof some concept in the environment (number of cans the robot has collected, for example).\nDoes such a feature used for representing the state space lead to a violation of the Markov\nproperty?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "Aslongasstatescontainadequateinformationsothattheconditionalprobabilitydistribution\nofthefuturestatesdependsonlyuponthecurrentstateoftheenvironment,anykindoffeature\ncan be used to describe the state space without violating the Markov property.",
    },
    {
        "question": "Which of the following will effect generalisation when using the tile coding method?",
        "options": [
            "modify the number of tiles in each tiling (assuming the range covered along each dimension by the tilings remains unchanged)",
            "modify the number of tilings",
            "modify the size of tiles",
            "modify the shape of tiles",
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "Option (a) and (c) are equivalent and effect the range over which values of one state gen-\neralise to values of other states. The same effect is also achieved by the number of tilings,\nsince, for example, more tilings (with different overlapping regions) will result in more states\nbeing affected by updates to the value of a single state. Finally, the shape of tiles has an\neffect on generalisation since it allows us to vary between uniform generalisation (for example\nusing square tiles) and non-uniform generalisation (for example using rectangular tiles) where\ngeneralisation is more pronounced along some dimensions and not so much along others.",
    },
    {
        "question": "For a particular MDP, suppose we use function approximation and using the gradient descent\napproach, converge to the value function that is the global optimum. Is this value function\nthe same, in general, as the true value function of the MDP?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "The value function corresponding to the global optimum and the true value function need not\nbe the same considering that, given the representation used, the function approximation may\nnot even be able to express the true value function.",
    },
    {
        "question": "Which of the following methods would benefit from normalising the magnitudes of the basis\nfunctions?",
        "options": [
            "on-line gradient descent TD(λ)",
            "linear gradient descent Sarsa(λ)",
            "LSPI",
            "none of the above",
        ],
        "correct": [0, 1],
        "explanation": "Order of magnitude differences in the values of the features can impact the performance of\ngradient descent procedures and hence such methods can benefit from normalisation of the\ninputs. On the other hand LSPI involves solving a system of linear equations, for which\nprocedures exist which are not impacted by scaling issues.",
    },
    {
        "question": "Suppose that individual features, φ (s,a), used in the representation of the action value func-\ni\ntion are non-linear functions of s and a. Is it possible to use the LSTDQ method in such\nscenarios?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "When discussing linear methods such as LSTDQ, we are talking about methods which can\napproximate functions which are linear in the parameter vector, not the feature vector.",
    },
    {
        "question": "Which among the following statements about the LSTD and LSTDQ methods is/are correct?",
        "options": [
            "LSTD learns the state value function",
            "LSTDQ learns the action value function",
            "both LSTD and LSTDQ can reuse samples",
            "both LSTD and LSTDQ can be used along with tabular representations of value functions",
        ],
        "correct": [0, 1, 3],
        "explanation": "Option (c) is not correct. Given a set of samples collected from the actual process (not from\na generative model in which case reusing samples is perhaps not that important) it is useful\nfor these samples to be reused in evaluating different policies. Recall that LSPI is a policy\n2\n\niterationalgorithm wherethe policy isconstantlybeingimprovedupon(and hencechanging).\nSuch sample reuse is possible in LSTDQ if for any policy π, π(s(cid:48)) is available for each s(cid:48) in\nthe set of samples. This is because for different policies, the same samples can be made use\nof, as individual policies only determine the φ(s(cid:48),π(s(cid:48))) component of A˜. This is not the case\nwith LSTD where freedom in action choices is not available and must be determined from the\npolicy that is being evaluated.",
    },
    {
        "question": "Consider the five state random walk task described in the book. There are five states,\n{s ,s ,...,s }, in a row with two actions each, left and right. There are two terminal states\n1 2 5\nat each end, with a reward of +1 for terminating on the right, after s and a reward of 0 for\n5\nall other transitions, including the one terminating on the left after s . In designing a linear\n1\nfunction approximator, what is the least number of state features required to represent the\nvalue of the equi-probable random policy?",
        "options": [
            "1",
            "2",
            "3",
            "5",
        ],
        "correct": 0,
        "explanation": "The value of the states from s to s are 1/6, 2/6, ..., 5/6. Hence a single feature, φ(s )=i is\n1 5 i\nadequate to represent the values.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 9 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W9_2026 = [
    {
        "question": "State True or False for the following statements:\nStatement 1: DQN is an on-policy technique.\nStatement 2: Actor-Critic is a policy gradient method.",
        "options": [
            "Both the statements are True.",
            "Statement 1 is True and Statement 2 is False.",
            "Statement 1 is False and Statement 2 is True.",
            "Both the statements are False.",
        ],
        "correct": 2,
        "explanation": "DQN uses Q learning, which is off-policy.\nActor-critic is based on policy gradient theorem(used in the actor training).",
    },
    {
        "question": "What are the reasons behind using an experience replay buffer in DQN?",
        "options": [
            "Random sampling from experience replay buffer breaks correlations among transitions.",
            "It leads to efficient usage of real-world samples.",
            "It guarantees convergence to the optimal policy.",
            "None of the above",
        ],
        "correct": [0, 1],
        "explanation": "Sampling randomly from replay buffer breaks the strong correlations between the transitions,\nleading to better updates in the neural network. Moreover, a sample can be used for more\nthan one update.",
    },
    {
        "question": "Statement: DQN is implemented with current and target network.\nReason: Using target network helps in avoiding chasing a non-stationary target.",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true, Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 0,
        "explanation": "The target network provides a stationary target for certain number of steps stabilizing the\nupdates in DQN",
    },
    {
        "question": "Policy gradient methods can be used for continuous action spaces.",
        "options": [
            "True",
            "False",
        ],
        "correct": 0,
        "explanation": "Aspolicygradientdirectlyapproximatethepolicyitself,theycanbeusedforcontinuousaction\nspaces.",
    },
    {
        "question": "Assertion: Actor-critic updates have lesser variance than REINFORCE updates.\nReason: Actor-critic methods use TD target instead of G .\nt",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true, Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 0,
        "explanation": "UsingG inREINFORCEinvolvesreturnsfromentiretrajectorywhichcauseshighervariance\nt\nin updates than TD-target in Actor-Critic.",
    },
    {
        "question": "Choose the correct statement for Policy Gradient Theorem for average reward formulation:",
        "options": [
            "∂ρ(π) =(cid:80) dπ(s)(cid:80) ∂π(s,a)\n∂θ s a ∂θ",
            "∂ρ(π) =(cid:80) vπ(s)(cid:80) ∂π(s,a)qπ(s,a)\n∂θ s a ∂θ",
            "∂ρ(π) =(cid:80) dπ(s)(cid:80) ∂π(s,a)qπ(s,a)\n∂θ s a ∂θ",
            "None of the above",
        ],
        "correct": 2,
        "explanation": "AsprovedinthevideoofREINFORCE,(c)representsthecorrectstatementofPolicyGradient\nTheorem",
    },
    {
        "question": "Suppose we are using a policy gradient method to solve a reinforcement learning problem.\nAssuming that the policy returned by the method is not optimal, which among the following\nare plausible reasons for such an outcome?",
        "options": [
            "The search procedure converged to a locally optimal policy.",
            "The search procedure was terminated before it could reach an optimal policy.",
            "Anoptimalpolicycouldnotberepresentedbytheparameterisationusedtorepresentthe\npolicy.",
            "None of these",
        ],
        "correct": [0, 1, 2],
        "explanation": "(a), (b) and (c) are all plausible reasons.",
    },
    {
        "question": "State True or False:\nMonte Carlo policy gradient methods typically converge faster than the actor-critic methods,\ngiven that we use similar parameterisations and that the approximation to the Qπ used in the\nactor-critic method satisfies the compatibility criteria.",
        "options": [
            "True",
            "False",
        ],
        "correct": 1,
        "explanation": "MCpolicygradientalgorithmsgenerallysufferfromlargevarianceduetolongepisodelengths\nwhichcanslowdownconvergence. Actor-criticmethods,byrelyingonvaluefunctionestimates\nlead to reduced variance, and hence, faster convergence.",
    },
    {
        "question": "When using policy gradient methods, if we make use of the average reward formulation rather\nthanthediscountedrewardformulation,thenisitnecessarytoassignadesignatedstartstate,\ns ?",
        "options": [
            "Yes",
            "No",
            "Can’t say",
        ],
        "correct": 1,
        "explanation": "We use the concept of a designated start state to allow a single value that can be assigned\nto a policy for evaluation. This is true for the average reward formulation even without a\ndesignated start state, by using the long term expected reward per step, ρ(π), where:\nρ(π)=lim 1E[r +r +...+r |π]\nN→∞ N 1 2 N",
    },
    {
        "question": "State True or False:\nExploration techniques like softmax (or other equivalent techniques) are not needed for DQN\nas the randomisation provided by experience replay provides sufficient exploration.",
        "options": [
            "True",
            "False",
        ],
        "correct": 1,
        "explanation": "Some technique to ensure exploration is still required. As with the original Q-learning algo-\nrithm, if we only consider greedy transitions with respect to the action-value function, a large\npart of the state space will likely remain unexplored.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 9 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W9_2025 = [
    {
        "question": "Which among the following is/are the advantages of using the Deep Q-learning method over\nother learning methods that we have seen?",
        "options": [
            "a faster implementation of the Q-learning algorithm",
            "guarantees convergence to the optimal policy",
            "obviates the need to hand-craft features used in function approximation",
            "allows the use of off-policy algorithms rather than on-policy learning schemes",
        ],
        "correct": 2,
        "explanation": "As we have seen with the Atari games example, the input to the network is raw pixel data\nfrom which the network manages to learn appropriate features to be used for representing the\naction value function.",
    },
    {
        "question": "In the Deep Q-learning method, is ϵ-greedy (or other equivalent techniques) required to ensure exploration, or is this taken care of by the randomisation provided by experience replay?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "Some technique to ensure exploration is still required. As with the original Q-learning algo-\nrithm,ifweonlyconsidertransitionsgeneratedbytheactionvaluefunction(whichisessentially\nwhat we’ll get with experience replay without any exploration), a large part of the state space\nwill likely remain unexplored.",
    },
    {
        "question": "Value function based methods are oriented towards finding deterministic policies whereas policy search methods are geared towards finding stochastic policies. True or false?",
        "options": [
            "false",
            "true",
        ],
        "correct": 1,
        "explanation": "Withvaluefunctionbasedmethods,policiesarederivedfromthevaluefunctionbyconsidering,\nforastate,thatactionwhichgivesmaximumvalue. Thisleadstoadeterministicpolicy. Onthe\nother hand, no such maximisation is at work in policy search methods, where the parameters\nlearned, using the gradient descent method, for example, determine the agent’s policy. This is\nlikely to be stochastic if the optimal policy (global or local) is stochastic.",
    },
    {
        "question": "Suppose we are using a policy gradient method to solve a reinforcement learning problem.\nAssuming that the policy returned by the method is not optimal, which among the following\nare plausible reasons for such an outcome?",
        "options": [
            "the search procedure converged to a locally optimal policy",
            "the search procedure was terminated before it could reach the optimal policy",
            "the sample trajectories arising in the problem were very long",
            "the optimal policy could not be represented by the parametrisation used to represent the\npolicy",
        ],
        "correct": [0, 1, 3],
        "explanation": "Option (c) may result in an increase in the time it takes to converge to a policy, but does not\nnecessarily affect the optimality of the policy obtained.",
    },
    {
        "question": "In using policy gradient methods, if we make use of the average reward formulation rather\nthan the discounted reward formulation, then is it necessary to consider, for problems that do\nnot have a unique start state, a designated start state, s ?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "We used the concept of a designated start state to allow a single value that can be assigned\nto a policy for the purpose of evaluation. The same result is obtained when using the average\nreward formulation, i.e, by using the average reward formulation we can compare policies\naccording to their long term expected reward per step, ρ(π), where\n1\nρ(π)=lim E{r +r +r +...+r |π}\nn→∞N 1 2 3 N",
    },
    {
        "question": "Using similar parametrisations to represent policies, would you expect, in general, MC policy\ngradient methods to converge faster or slower than actor-critic methods assuming that the\napproximation to Qπ used in the actor-critic method satisfies the compatibility criteria?",
        "options": [
            "slower",
            "faster",
        ],
        "correct": 0,
        "explanation": "As we have seen, MC policy gradient algorithms may suffer from large variance due to long\nepisode lengths which can slow down convergence. Actor-critic methods, by relying on value\nfunction estimates can lead to reduced variance, and hence, faster convergence.",
    },
    {
        "question": "If f approximates Qπ and is compatible with the parameterisation used for the policy, then\nw\nthis indicates that we can use f in place of Qπ in the expression for calculating the gradient\nw\nof the policy performance metric with respect to the policy parameter because",
        "options": [
            "Qπ(s,a)−f (s,a)=0 in the direction of the gradient of f (s,a)\nw w",
            "Qπ(s,a)−f (s,a)=0 in the direction of the gradient of π(s,a)\nw",
            "theerrorbetweenQπ andf isorthogonaltothegradientofthepolicyparameterisation\nw",
        ],
        "correct": [1, 2],
        "explanation": "As indicated by options (b) & (c), we can use f in place of Qπ if the difference between the\nw\ntwo is zero in the direction of the gradient of π(s,a).",
    },
    {
        "question": "Suppose we use the actor-critic algorithm described in the lectures where Qπ is approximated\nand the approximation used is compatible with the parametrisation used for the actor. As-\nsuming the use of differentiable function approximators, we can conclude that the use of such\na scheme will result in",
        "options": [
            "convergence to a globally optimal policy",
            "convergence to a locally optimal policy",
            "cannot comment on the convergence of such an algorithm",
        ],
        "correct": 1,
        "explanation": "The idea behind the two theorems (policy gradient and policy gradient with function approx-\nimation) that we saw in the lectures is to show that using such an approach will result in the\npolicy converging. However, we can only prove convergence to a locally optimal policy.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 10 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W10_2026 = [
    {
        "question": "Consider the update equation for SMDP Q-learning:\nQ(s,a)=Q(s,a)+α[A+Bmax Q(s′,a′)−Q(s,a)]\na′\nWhich of the following are the correct values of A and B ?\n(r is the reward received at time step k, and γ is the discount factor)\nk",
        "options": [
            "A = r ; B = γ\nt",
            "A = r +γr +...+γτ−1r ; B = γτ\nt t+1 t+τ",
            "A = γtr +γt+1r +...+γt+τ−1r ; B = γt+τ\nt t+1 t+τ",
            "A = γτ−1r ; B = γτ\nt+τ",
        ],
        "correct": 1,
        "explanation": "Aisthevalueoftotaldiscountedrewardaccumulatedbetweentimesteptandtimestept+τ.\nDiscounting starts from the t + 1 step in the recursive formulation. B is the value of the\ndiscount factor after τ time steps =γτ.\nRefer to the lecture on SMDP Q-learning.",
    },
    {
        "question": "Consider a SMDP in which the next state and the reward only depend on the previous state\nand action i.e P(s′,τ|s,a)=P(s′|s,a)P(τ|s,a), R(s,a,τ,s′)=R(s,a,s′).\nIfwesolvetheaboveSMDPwithconventionalQ-learningwewillendupwiththesamepolicy\nas solving it with SMDP Q-learning.",
        "options": [
            "yes, because now τ won’t change anything and we end up with same states and action\nsequences",
            "no, becauseτ stilldependsonthestate, actionpairanddiscountingmayhaveaeffecton\nthe final policies.",
            "no, because the next state will still depend on the τ.",
            "yes, because the bellman equation is same for both methods in this case.",
        ],
        "correct": 1,
        "explanation": "The bellman equation for SMDP has γτ factor which will affect the returns and thus affect\nthe policy.",
    },
    {
        "question": "In HAM, what will be the immediate rewards received between two choice states.",
        "options": [
            "Accumulation of immediate rewards of the core MDP obtained between these choice\npoints.",
            "The return of the next choice state.",
            "The reward of only the next primitive action taken.",
            "Immediate reward is always zero",
        ],
        "correct": 0,
        "explanation": "The transaction between two choice states may involve going through multiple primitive\nstates.Therewardwillbeaccumulatingofalltherewardsobtainedaftertakingtheseprimitive\nactions.",
    },
    {
        "question": "Which of the following is true about Markov and Semi Markov Options?",
        "options": [
            "In a Markov Option the option’s policy depends only on the current state.",
            "In a Semi Markov Option the option’s policy can depend only on the current state.",
            "In a Semi Markov Option, the option’s policy may depend on the history since the exe-\ncution of the option began.",
            "A Semi-Markov Option is always a Markov Option but not vice versa.",
        ],
        "correct": [0, 1, 2],
        "explanation": "In Semi-Markov options, the policy π depends on all the states since the option started",
    },
    {
        "question": "Consider the two statements below for an SMDP for a HAM:\nStatement1: The state of the SMDP is defined by the state of the base MDP, the call stack\nand the state of the machine currently executing.\nStatement2: The actions of the SMDP can only be defined by the action states.\nWhich of the following are true?",
        "options": [
            "Statement1 is True and Statement2 is True.",
            "Statement1 is True and Statement2 is False.",
            "Statement1 is False and Statement2 is True.",
            "Statement1 is False and Statement2 is False.",
        ],
        "correct": 1,
        "explanation": "The actions are defined by the states that can be transitioned to from each choice state.",
    },
    {
        "question": "Which of the following are possible advantages of formulating a given problem as a hierarchy\nof sub-problems?",
        "options": [
            "A reduced state space.",
            "More meaningful state-abstraction.",
            "Temporal abstraction of behaviour.",
            "Re-usability of learnt sub-problems.",
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "(a) and (b) are true. By solving sub-problems independent of the overall-problem, we can\nreducethesizeofthestatespace,andusemoremeaningfulstaterepresentations-encapsulating\nonly that information required to solve each sub-problem. (c) is true. We abstract away the\nnotion of time, as we deal with multiple sub-problems, each of which could take a varying\namount of time.\n(d) is true. We can reuse the policies learnt for repeated sub-problems in the hierarchy.",
    },
    {
        "question": "In SMDP, consider the case when τ is fixed for all state, action pairs. Will we always get the\nsame policy for conventional Q-learning and SMDP Q learning then? Provide answer for the\nthree cases when τ =3, τ =2, τ =1.",
        "options": [
            "yes, yes, no",
            "no, no, no",
            "yes, yes, yes,",
            "no, no, yes",
        ],
        "correct": 3,
        "explanation": "For τ ̸=1 then the discounting changes and thus the policy.",
    },
    {
        "question": "State True or False:\nIn the classical options framework, each option has a non-zero probability of terminating in\nany state of the environment.",
        "options": [
            "True",
            "False",
        ],
        "correct": 1,
        "explanation": "In the classical options framework, each option assigns a probability with which it will termi-\nnate to every state of the environment. However, the probability of termination can be zero\nfor any number of these states.",
    },
    {
        "question": "Suppose that we model a robot in a room as an SMDP, such that the position of the robot in\nthe room is the state of the SMDP. Which of the following scenarios satisfy the assumption\nthat the next state and transition time are independent of each other given the current state\nandactioni.eP(s′,τ|s,a)=P(s′|s,a)P(τ|s,a)? (Assumethatprimitiveactions-<left,right,\nup, down> take a single time step to execute.)",
        "options": [
            "The room has a single door. The actions available are : {exit the room, move left, move\nright, move up, move down}.",
            "The room has a two doors. The actions available are : {exit the room, move left, move\nright, move up, move down}.",
            "The room has a two doors. The actions available are: {move left, move right, move up,\nmove down}.",
            "None of the above.",
        ],
        "correct": [0, 2],
        "explanation": "The assumption holds for (a). There is only one way to exit the room, so the transition time\ntakentoexittheroomisindependentofthenextstate, providedthecurrentstateandaction.\nThe assumption does not hold for (b). The transition time taken to exit the room depends on\nwhich door the robot uses (that is, it depends on the next state).\nThe assumption holds for (c). Only primitive actions available, each primitive action has a\ntransition time of a single time step.",
    },
    {
        "question": "Which of the following is a correct Bellman equation for an SMDP?\nNote: R(s,a,s′) =⇒ reward is a function of only s,a and s′.",
        "options": [
            "V∗(s)=max [R(s,a,τ,s′)+γτP(s′|s,a)V∗(s′)]\na∈A(S)",
            "V∗(s)=max [Σ P(s′|s,a,τ)(R(s,a,τ,s′)+γV∗(s′))]\na∈A(S) s′,τ",
            "V∗(s)=max [Σ P(s′,τ|s,a)(R(s,a,τ,s′)+γτV∗(s′))]\na∈A(S) s′,τ",
            "V∗(s)=max [Σ P(s′,τ|s,a)(R(s,a,s′)+γV∗(s′))]\na∈A(S) s′,τ",
        ],
        "correct": 2,
        "explanation": "Reward depend on s, a, s′, τ. We reach next state after τ time so we discount by γτ. Refer\n”Recent advances in hierarchical reinforcement learning” paper for more information.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 10 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W10_2025 = [
    {
        "question": "Suppose that in solving a problem, we make use of state abstraction in identifying solutions\nto some of the sub-problems. In this approach, is it possible to obtain a recursively optimal\nsolution to the original problem?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "A recursively optimal solution to a hierarchical RL problem can be obtained by combining\nthe optimal solutions of all sub-problems. An abstraction is called safe if optimal solutions in\nthe abstract space are also optimal in the original space. Essentially, when performing state\nabstraction,ifweincludeallrelevantfeatures,thentheoptimalsolutionsintheabstractspace\nwillremainoptimalintheoriginalspace. Thus,usingsuchabstractionswillallowustoobtain\nsolutions to the original problem which are recursively optimal.",
    },
    {
        "question": "What kind of solution would you expect to obtain if, in solving a problem, policies for each\nindividual sub-problem are learned in isolation (i.e., without taking into consideration the\noverall problem)?",
        "options": [
            "hierarchically optimal solution",
            "recursively optimal solution",
            "flat optimal solution",
        ],
        "correct": 1,
        "explanation": "In isolation, the best you can expect to do is solve each sub-problem optimally. Combining\nsuch policies for the sub-problems of a given hierarchical problem will generally result in a\nrecursively optimal solution.",
    },
    {
        "question": "DothepoliciesofindividualoptionsneedtobedefinedovertheentirestatespaceoftheMDP\n(of the original problem)?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "If the termination condition for a particular state is equal to 1, then there is no need for the\noption policy to be defined over this state. Additionally, by setting the termination condition\nappropriately, it should be clear that the set of states which the corresponding option can be\nactive in can be controlled and can be designed to be only a subset of the original state space.\nHence, the policy of an option does not necessarily need to be defined over the entire state\nspace.",
    },
    {
        "question": "Consider the two room example discussed in the lectures. Suppose you define two options,\nO , to take the agent in room 1 (the left room) to room 2, and O , to take the agent in\n1 2\nroom 2 to the goal state. Assuming that you have appropriately specified the initiation sets\nand termination conditions for both the options and are trying to learn the individual option\npolicies, would you need to use SMDP Q-learning or would conventional Q-learning suffice?",
        "options": [
            "SMDP Q-learning",
            "conventional Q-learning",
        ],
        "correct": 1,
        "explanation": "Since neither option invokes the other in this example, each option’s policy comprises of se-\nlecting primitive actions only, and hence, SMDP Q-learning is not required.",
    },
    {
        "question": "Consider a Markov policy over options µ : S×O → [0,1], where S is the set of states and O\nis the set of options. Assume that all options are Markov. While the policy µ selects options,\nbyconsideringtheprimitiveactionsbeingselectedinthoseoptions, wecandetermineanother\npolicy, π, which corresponds to µ, but is a conventional policy over actions. In general, will π\nalso be a Markov policy?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "When considering the conventional policy, π, the action selected in state s depends not only\nt\non the current state (s ), but also on the option being followed at that time, which essentially\nt\ndepends on the entire history since the policy µ was initiated.",
    },
    {
        "question": "Considerthefollowingproblemdesign. Youhaveagridworldwithseveralrooms,asdiscussed\nin the lectures, with the goal state in a corner cell of one of the rooms. You set up an agent\nwith options for exiting each of the rooms into the other. You also allow the agent to pick\nfrom the four primitive actions. There is a step reward of -1. The learning algorithm used is\nSMDP Q-learning, with normal Q-learning updates for the primitive actions. You expect the\nagent to learn faster due to the presence of the options, but discover that it is not the case.\nCan you explain what might have caused this?",
        "options": [
            "the options are not useful for solving the problem, hence the slowdown",
            "initially, the agent will focus more on using primitive actions, causing slowdown",
            "due to the presence of options, we can no longer achieve the optimal solution, hence it\ntakes longer",
            "it takes longer because we are using SMDP Q-learning compared to conventional Q-\nlearning which is faster",
        ],
        "correct": 1,
        "explanation": "Consider the contrast between selecting a primitive action and an option during the initial\nphase of learning in this problem. On selecting a primitive action from states near the start\nstate or a doorway state, you do not reach the goal state and get a unit of negative reward.\nOn selecting an option, however, you are transported to some doorway state (which is not\nthe goal state) and get a negative reward of larger magnitude (recall SMDP rewards). This\nsuggests that initially, the primitive options will appear more promising and will be explored\nmore whereas the benefit of the options will not initially be realised or exploited. Thus, the\nexpected speedup would in general not be observed.",
    },
    {
        "question": "Usingintra-optionlearningtechniques,wecanlearnaboutoptionsevenwithouteverexecuting\nthem. True or false?",
        "options": [
            "false",
            "true",
        ],
        "correct": 1,
        "explanation": "As we have seen, in intra-option learning, we can update estimates of multiple options based\non observing the rewards received on executing a single option. Many of the options whose\nestimates are updated need not even have been executed.",
    },
    {
        "question": "Suppose that you have identified a set of sub-tasks for solving a large problem using the\nhierarchical learning approach. To solve each sub-task efficiently, you want to constrain the\nprimitive actions that can be executed within each sub-task. Specifying such constraints is\npossible in",
        "options": [
            "options",
            "HAMs",
            "both",
        ],
        "correct": 2,
        "explanation": "Specifying the option policies allows us to constrain the primitive actions that are executed in\neach option/sub-task. Similar effect can be obtained in HAMs by limiting the choice states in\neach machine.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 11 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W11_2026 = [
    {
        "question": "Which of the following option is correct for the sub-task terminations in the MAXQ Frame-\nwork?",
        "options": [
            "The termination is stochastic",
            "The termination is deterministic",
        ],
        "correct": 1,
        "explanation": "As discussed in the lectures, for each sub-task, all states of the core MDP are partitioned into\na set of active states and a set of terminal states, where sub-task termination is immediate\n(and deterministic) whenever a terminal state is entered.",
    },
    {
        "question": "In MAXQ learning, we have a collection of SMDPs. In conventional value function, the only\nargument was state. In MAXQ value function decomposition, we have value function of the\nform Vπ(i,s), where π is the policy, s is the current state. What is ’i’ supposed to be in the\nabove notation?",
        "options": [
            "The number of times we have visited state s",
            "It means it is ith iteration of updates",
            "i is the identity of the sub-task/SMDP.",
            "None of the above.",
        ],
        "correct": 2,
        "explanation": "From the notations followed in lectures as well as reference, Vπ(i,s) is the value of state s in\ntask ’i’. Where ’i’ can be though of as one of the SMDP from the collection of the SMDPs.\nComprehensive model for question 3 to question 6\nConsider the following taxi-world problem. The grey colored cell are inaccessible cells or can\nbethoughtofobstacles. ThecornercellsmarkedasR,G,B,Yareallowedpickup-droppoints\nfor passengers.\nR Y\nG B\nSay following is the Call-Graph for the above Taxi-World problem.\n1\n\nRoot\nPick up Drop off\nput-\npick-up Navigate(t)\ndown\nUp Down Left Right",
    },
    {
        "question": "From the below list of actions:\ni Left\nii Drop off\niii Navigate\niv put-down\nWhich among them are the primitive actions?",
        "options": [
            "i, ii, iii, iv",
            "ii, iii",
            "i, iv",
            "None of the above",
        ],
        "correct": 2,
        "explanation": "Refer to video of MAXQ for understanding call-graphs. primitive actions are actions actually\npresent in the MDP.",
    },
    {
        "question": "From the discussion in the class, it is said that Navigate is not a single sub-task. What is the\nparameter ’t’ in ’Navigate(t)’ from the class discussions?",
        "options": [
            "the number of times ’Pick up’ or ’Drop off’ have called sub-task Navigate",
            "the maximum number of primitive actions permitted to finish sub-task",
            "the destination (in this case, one of R, G, B, Y)",
            "None of the above",
        ],
        "correct": 2,
        "explanation": "Please refer to the video titled ’MAXQ’ of week 11.",
    },
    {
        "question": "State True/False. The ordering of the above call-graph is important and sub-tasks should be\nperformed via these orderings.",
        "options": [
            "True",
            "False",
        ],
        "correct": 1,
        "explanation": "The ordering is not particularly important in solving the problem. It is for pictorial ease.",
    },
    {
        "question": "Suppose the passenger is always either inside the taxi or at one of the four pickup/dropoff\nlocations. That means there are 5 states for passenger’s location. Then for the given taxi-\nworld, what is the number of states that suffices to define all information?",
        "options": [
            "18",
            "18*5",
            "18*5*4",
            "None of the above",
        ],
        "correct": 2,
        "explanation": "number of possible states for taxi is 18. (7 cells are inaccessible in grid out of 25). Number of\nlocations for a passenger is 5. There are 4 possible destination for a passenger. So total states\nare 18*5*4.",
    },
    {
        "question": "State True/False. Bottlenecks are useful surrogative measures for option discovery.",
        "options": [
            "True",
            "False",
        ],
        "correct": 0,
        "explanation": "Refer to the lecture.",
    },
    {
        "question": "Which of the following can be considered as a good option in Hierarchical RL?",
        "options": [
            "An option that can be reused often",
            "An option that can cut down exploration",
            "An option that helps in transfer learning",
            "None of the above",
        ],
        "correct": [0, 1, 2],
        "explanation": "Refer to the lecture on Option Discovery.",
    },
    {
        "question": "We define the action value for MAXQ as qπ(i,s,a) = vπ(a,s)+Cπ(i,s,a) where qπ(i,s,a)\ncan be interpreted as expected return when you are in sub-task i, and state s, and you decide\nto perform sub-task a. Assume that in taking a, you get reward r₁, and after completion of a, you get reward r₂ in completing sub-task i. Choose the correct value of Cπ(i,s,a) from the following.",
        "options": [
            "Cπ(i,s,a)=r",
            "Cπ(i,s,a)=r +r\n1 2",
            "Cπ(i,s,a)=r",
            "None of the above",
        ],
        "correct": 0,
        "explanation": "what we defined as r in the question is nothing but vπ(a,s).\n1\nanditshouldbeclearfromintuitivedefinitionofactionvaluefunctionthatqπ(i,s,a)=r +r .\n1 2\nThus, Cπ(i,s,a)=r .",
    },
    {
        "question": "In the MAXQ approach to solving a problem, suppose that sub-task M invokes sub-task M .\ni j\nDo the pseudo rewards of M have any effect on sub-task M ?\nj i",
        "options": [
            "Yes",
            "No",
        ],
        "correct": 0,
        "explanation": "The pseudo rewards of one sub-task are not directly considered when solving a different sub-\ntask regardless of their connectivity. However, the policy learned for M using the pseudo\nj\nrewards may effect the sub-task M .\ni",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 11 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W11_2025 = [
    {
        "question": "Using the MAXQ approach leads to solutions which are",
        "options": [
            "hierarchically optimal",
            "recursively optimal",
            "flat optimal",
        ],
        "correct": 1,
        "explanation": "Since the MAXQ policy of the core MDP is the set of policies of individual sub-tasks, with\nindividual sub-task policies aiming to solve the sub-tasks optimally, you can expect to obtain\nrecursively optimal solutions using the MAXQ approach.",
    },
    {
        "question": "We saw that each sub-task has an associated pseudo-reward function. Are the rewards of the\ncore MDP available to the agent while it is learning policies of individual sub-tasks or is the\nagent restricted to the corresponding sub-task’s pseudo rewards?",
        "options": [
            "only pseudo rewards are available",
            "both pseudo rewards and core MDP rewards are available",
        ],
        "correct": 1,
        "explanation": "As we observed in the example taxi problem, rewards of the core MDP are available while\nlearning the policies of the sub-tasks.",
    },
    {
        "question": "In the MAXQ framework, is termination in a sub-task deterministic or stochastic as in the\noptions framework?",
        "options": [
            "deterministic",
            "stochastic",
        ],
        "correct": 0,
        "explanation": "We saw in the sub-task definition that for each sub-task, all states of the core MDP are\npartitioned into a set of active states and a set of terminal states, where sub-task termination\nis immediate (and deterministic) whenever a terminal state is entered.",
    },
    {
        "question": "Each sub-task M is an SMDP because\ni",
        "options": [
            "the state space of the sub-task is a subset of the state space of the core MDP",
            "each sub-task has its own policy",
            "actions in a sub-task can be temporally extended",
            "the rewards received in sub-tasks depend not only on the state but also on the sub-task\nin which an action was executed",
        ],
        "correct": 2,
        "explanation": "In the definition, we saw that the actions in a sub-task comprise both, primitive actions as\nwell as other sub-tasks. The invocation of a sub-task results in a sequence of actions being\nexecuted (similar to an option). Thus, each sub-task is an SMDP.",
    },
    {
        "question": "TheexpectedrewardfunctionR¯(s,a)oftheSMDPcorrespondingtosub-taskM isequivalent\ni\nto the projected value function Vπi(a,s). True or false?",
        "options": [
            "false",
            "true",
        ],
        "correct": 0,
        "explanation": "Recall that R¯(s,a)=Vπ(a,s) not Vπi(a,s).",
    },
    {
        "question": "In the MAXQ approach to solving a problem, suppose that sub-task M invokes sub-task M .\ni j\nDo the pseudo rewards of M have any effect on sub-task M ?\nj i",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "The pseudo rewards of one sub-task are not directly considered when solving a different sub-\ntask regardless of their connectivity. However, since sub-task M invokes sub-task M , and\ni j\nhence depends upon the policy of M , the rewards of M do effect sub-task M , as the pseudo\nj j i\nrewards of sub-task M would be a factor determining the policy of M .\nj j",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 12 (2026)
# ─────────────────────────────────────────────────────────────────────────────
W12_2026 = [
    {
        "question": "Consider an environment in which an agent is randomly dropped into either state s₁ or s₂ with equal probability. The agent can only view obstacles present immediately to the North, South, East or West. However the observation made in each direction by the agent may be wrong with a probability of 0.1. If in state s₁ obstacles are present to the North and South, and in s₂ obstacles are present to the East and West, what is the probability of the agent being in state s₁ if the observation made is that there are obstacles present to the North and West?",
        "options": [
            "81/82",
            "41/82",
            "73/82",
            "None of the above.",
        ],
        "correct": 1,
        "explanation": "Application of Bayes Rule.P(A|B) = P(B|A)P(A) with A being the ”Present in\nP(B|A)P(A)+P(B|¬A)P(¬A)\nstate s ” and B being ”Observed obstacles to the North and West. Ans = 0.5”",
    },
    {
        "question": "In the same environment as Question 1, suppose state s₁ has obstacles present only to the North and South, and s₂ has obstacles present only to the East and West. What is the probability of the agent being in state s₁ if the observation made is that there are obstacles present only to the North, East and West?",
        "options": [
            "81/82",
            "41/82",
            "73/82",
            "None of the above.",
        ],
        "correct": 3,
        "explanation": "Application of Bayes Rule.P(A|B) = P(B|A)P(A) with A being the ”Present in\nP(B|A)P(A)+P(B|¬A)P(¬A)\nstate s ” and B being ”Observed obstacles to the North, East. Ans: 1/82”",
    },
    {
        "question": "Assertion: One of the reasons that history-based methods are not feasible is because of the\nsignificant increase in the state space size when the trajectory is long.\nReason: The number of states increases polynomially w.r.t. trajectory length.",
        "options": [
            "Both Assertion and Reason are true, and Reason is correct explanation for Assertion.",
            "Both Assertion and Reason are true, but Reason is not correct explanation for assertion.",
            "Assertion is true, Reason is false",
            "Both Assertion and Reason are false",
        ],
        "correct": 2,
        "explanation": "The assertion is true, the number of states increases significantly with trajectory length, how-\never it is due to the exponential increase in the number of states that history-based methods\nare not feasible.",
    },
    {
        "question": "In the case of POMDPs, which of the following is a good estimate of the return of a trajectory of a policy π, given the current belief state and the solution to the underlying MDP (value function for all states)?",
        "options": [
            "Average of all Vπ(s) where b(s)>0.",
            "Weighted average of all Vπ(s) where b(s) are the weights.",
            "Average of all Vπ(s) where b(s)≥α, where α is a small positive value",
            "None of the above",
        ],
        "correct": 1,
        "explanation": "It is equivalent to the expected value of the return, making it a good estimate of the return of\nthe current trajectory.",
    },
    {
        "question": "Consider the grid-world shown below:\nWalls and obstacles are colored gray. The agent is equipped with a sensor that can detect the\npresence of walls or obstacles immediately to its North, South, East or West.\nWhich of the following are true if we represent states by their sensor observations?",
        "options": [
            "The grid-world is a 1st-order Markov system.",
            "The grid-world is a 2nd-order Markov system.",
            "The grid-world is a 3rd-order Markov system.",
            "The grid-world is a 4th-order Markov system.",
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "Each state is uniquely identifiable from the sensor reading. A system that is 1st order Markov\nis necessarily 2nd, 3rd and 4th order Markov.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# WEEK 12 (2025)
# ─────────────────────────────────────────────────────────────────────────────
W12_2025 = [
    {
        "question": "In the partial observability example that we saw, there were some observations which uniquely identify the state of the environment. Suppose in a problem, no such observations exist, i.e.,\nthere are no observations which allow us to exactly determine the state of the environment.\nIn such problems, is it ever possible to be sure which state you are in given only the sequence\nof observations?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 1,
        "explanation": "It is not necessary that there exist observations that uniquely identify the state of the sys-\ntem. In many problems, the sequence of observations suffice to determine with certainty, the\nstate of the system. For example, in a problem, a particular observation may correspond to\nmultiple states. However, it is possible that the sequence of observations that precede such\nan observation allows us to distinguish between the multiple states which that observation\ncorresponds to. In addition, the agent has knowledge of its actions which can further help\nmake such distinctions.",
    },
    {
        "question": "Suppose that some of the actions that are available to an agent in a partially observable\nenvironment have non-deterministic outcomes. How would this impact the agent’s ability to\ndetermine the state it is in?",
        "options": [
            "it would make determining the state easier",
            "it would make determining the state harder",
            "it would have no effect in determining the state",
        ],
        "correct": 1,
        "explanation": "Non-deterministic action outcomes introduce another layer of uncertainty, since the agent can\nnow not be sure what the effect of taking an action in a state is (as the observations do not\nallow the agent to deterministically evaluate the state to which the agent transitions to after\ntaking an action). This would generally make the problem of state determination harder.",
    },
    {
        "question": "Referring to the partial observability example considered in the lectures and assuming that\nthere is no noise in the sensor outputs, is it true that all observation sequences of length 3\nor more result in the elimination of uncertainty regarding the position of the agent in the\nenvironment?",
        "options": [
            "no",
            "yes",
        ],
        "correct": 0,
        "explanation": "Consider the plausible sequence of observations 1010, 1010, 1010, 1010.",
    },
    {
        "question": "To solve a POMDP problem, suppose you decide to maintain belief states. Would the estima-\ntion of the belief states benefit from access to the history of observations and/or actions?",
        "options": [
            "access to past observations, but not actions, would improve belief state estimation",
            "access to past actions, but not observations, would improve belief state estimation",
            "access to past observations and actions would improve belief state estimation",
            "access to past observations or actions will not improve belief state estimation",
        ],
        "correct": 3,
        "explanation": "An agent needs to update its belief upon taking an action and observing the corresponding\nobservation. Since the state is Markovian, maintaining a belief over the states solely requires\nknowledge of the previous belief state, the action taken, and the current observation. The\ninformation from past actions and observations is already encapsulated in the belief state.",
    },
    {
        "question": "Suppose that you are given a problem in which the agent is able to determine the state it\ntransitions to after each action taken by the agent. However, the state space is described in a\nmanner which requires the agent to consider information in the current, as well as the latest\npast state in the sequence, to make action decisions. Is the problem so defined an MDP, a\nPOMDP, or neither? Can this problem be solved using RL techniques that we have studied\n(perhaps with possible modifications to the problem definition)?",
        "options": [
            "MDP, yes",
            "POMDP, yes",
            "neither, no",
            "neither, yes",
        ],
        "correct": 3,
        "explanation": "TheproblemsodefinedisneitheranMDP(theMarkovpropertydoesnothold)noraPOMDP\n(partial observability is not an issue here). We can reformulate the problem by considering\na state in the new formulation to be a subset of the set of all pairs of states in the original\nformulation. With appropriate modifications to the transition probability and reward func-\ntion, we can obtain a MDP which can be solved using the various RL techniques that we\nhave seen. Another approach would be to consider this problem as a POMDP where each\n‘observation’ gives only partial information regarding the ‘state’ of the system and use history\nbased methods.",
    },
    {
        "question": "Recall the example partially observable environment encountered in the lectures. Suppose\nthe goal in this problem is to reach the bottom-right state, with the usual -1 rewards for\neach transition. Assume that the agent starts two cells below the top left state and the first\naction selected by the QMDP procedure is to move down. Assuming deterministic action\noutcomes with no noise in the observations, as well as the use of the QMDP procedure where\nthe underlying MDP has been correctly solved, what can you say about the optimality of the\nagent’s policy in this scenario?",
        "options": [
            "the agent will follow an optimal policy to reach the goal",
            "the agent’s policy to reach the goal will not be optimal",
            "the optimality of the agent’s policy towards reaching the goal in this scenario cannot be\ndetermined with certainty",
        ],
        "correct": 0,
        "explanation": "Note that on taking its first action, the agent reaches a state which is uniquely identifiable by\nthe the observation corresponding to that state. Thus, the first action of the agent dispels all\nstate uncertainty and this allows the QMDP procedure to follow the optimal policy to reach\nthe goal.",
    },
]


WEEK_META = {
    "Week 1":  {"title": "Introduction to RL & Multi-Armed Bandits",           "icon": "📊", "tag": "W01"},
    "Week 2":  {"title": "Advanced Bandit Algorithms (UCB, Thompson, PAC)",     "icon": "📈", "tag": "W02"},
    "Week 3":  {"title": "Policy Gradient & Contextual Bandits",                "icon": "🔍", "tag": "W03"},
    "Week 4":  {"title": "MDPs, Bellman Equations & Value Functions",           "icon": "⚙️", "tag": "W04"},
    "Week 5":  {"title": "Dynamic Programming & Monte Carlo Methods",           "icon": "🔄", "tag": "W05"},
    "Week 6":  {"title": "TD Learning, SARSA & Q-Learning",                    "icon": "⚡", "tag": "W06"},
    "Week 7":  {"title": "Eligibility Traces & n-Step Methods",                "icon": "📎", "tag": "W07"},
    "Week 8":  {"title": "Function Approximation & LSTD",                      "icon": "🧮", "tag": "W08"},
    "Week 9":  {"title": "DQN, Actor-Critic & Policy Gradient Methods",        "icon": "🤖", "tag": "W09"},
    "Week 10": {"title": "SMDPs, Options & Hierarchical RL",                   "icon": "🏗️", "tag": "W10"},
    "Week 11": {"title": "MAXQ & Hierarchical Decomposition",                  "icon": "🌲", "tag": "W11"},
    "Week 12": {"title": "Partial Observability & POMDPs",                     "icon": "👁️", "tag": "W12"},
}

QUIZ_DATA = {}
for i in range(1, 13):
    wk = f"Week {i}"
    q2026 = eval(f"W{i}_2026")
    q2025 = eval(f"W{i}_2025")
    QUIZ_DATA[wk] = {
        "title": WEEK_META[wk]["title"],
        "icon": WEEK_META[wk]["icon"],
        "tag": WEEK_META[wk]["tag"],
        "week_num": i,
        "2026": q2026,
        "2025": q2025,
        "mixed": q2026 + q2025,
    }
