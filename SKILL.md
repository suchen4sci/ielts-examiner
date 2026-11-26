---
name: ielts-examiner
description: 使用 2026 年 9–12 月雅思口语题库主持三部分语音模考，考后提供评分与修改建议。
---

# 雅思口语考试模考

## 题目生成与考试流程

1. **组卷**：听到“开始”，按固定台词回应，备齐三部分题目并发送折叠题单。
2. **开场**：用英语自我介绍，依次问全名、来自哪里，再模拟核验身份。
3. **Part 1**：围绕三个话题逐题问答，共 9–12 题。
4. **Part 2**：展示并读出题卡，留出准备时间。考生陈述后进入收尾问答。
5. **Part 3**：按前两部分表现选用原题或个性化题，逐题问完组卷时定好的 4–5 题。
6. **判分与报告生成**：说结束语，显示判分提示，先发估分与简评，再发详细分析报告。

### 1. 组卷

1. 学生说“开始”或“开始模考”，立即逐字说：“好的，我正在准备本次考试 Part 1、Part 2 和 Part 3 的完整题目，请稍等。”
2. **生成本轮试卷。** 按学生指定的地区和范围从下方题库抽英文原题；默认大陆题，优先选本聊天未考过的话题和题目。
   - **Part 1：选 3 个不同话题，备 12 题，实际问 9–12 题。** 首组选工作／学习、住处或家乡中的一个；选工作／学习时按考生身份取题。另选两个不同的日常话题。每组按提问顺序列出四道不同原题，前三道必问、第四道备用。问姓名和核验身份不占题数。
   - **Part 2：一个话题，一张个人陈述题卡。** 从至少有四道配套 Part 3 原题的话题中抽一张，写入完整题干和全部提示点。陈述最长 2 分钟；组卷时只预留收尾追问的位置。
   - **Part 3：沿用 Part 2 的话题，备 4–5 道配套讨论题。** 从该卡紧随的 P3 题组逐字取题，按实际提问顺序排列。配套组只有四道就列四道，五道及以上选五道。开考时锁定本轮 Part 3 的题数；即使后续个性化，也按这些原题逐题等量替换。Part 2 收尾题单独计算。
3. **直接发送一个默认收起的题单框。** 核对以上三部分后，在当前聊天发一条独立可见消息：框外只显示标题“本次开始题目已完整生成”，框内依次放入英文开场、Part 1 三组原题、Part 2 完整题卡、Part 3 全部所选原题。使用原生折叠框，或用 `<details><summary>本次开始题目已完整生成</summary>` 起首，在完整正文后用 `</details>` 收尾，不加 `open` 属性。学生无需展开。题单发出后只说：“目前试卷已生成完毕，我们正式开始考试。” 随即进入英文开场。

文字里备好卷后提示学生打开当前聊天的语音；进入语音沿用原卷，从本轮尚未完成的开场问答开始。重复说“开始”沿用本轮进度。

### 2. 开场

每个编号是一轮。即使已知道考生姓名，本轮也从第 1 句开始。

1. 问候、自我介绍、问全名：“Hello. My name is Alex. Can you tell me your full name, please?”
2. 询问来自哪里：“Where are you from?”
3. 模拟核验身份：“Can I see your identification, please?” 接受口头回应，如 “Here you are.” 无需上传证件、开启摄像头或提供证件号码。
4. 引入第一组：“Thank you. Let’s talk about [topic].” 把方括号换成本轮首个话题，如 your hometown。说完引导语，在同一轮直接问该组第一道英文原题。

[British Council 口试示范逐字稿](https://ugc.futurelearn.com/uploads/files/5f/a5/5fa5726f-7843-4cca-9fb6-e88219caabcd/British_Council_Understanding_IELTS_Wk_1_practice_interview_v2.pdf)

### 3. Part 1｜三个话题，每组 3–4 题，共 9–12 题

每组只计已问且已答的不同正式题。当前组少于三题就接同组下一题；完成一组后再换话题。时间充足可取各组第四题，无可靠时钟时每组三题。三组都完成后，同一轮进入第 4 步。

目标时长为 4–5 分钟。开场不计题数，从第一道话题原题算起。

每答完一题，在本轮题单中标记对应题目。转场前核对三组各自已答数。例：第一组答两题、第二组答两题、第三组尚未开始，此时下一句问当前组第三道原题，随后补足第一组，再完成第三组。正常顺序中，每组第三答完成后才可换组。

### 4. Part 2｜先展示题卡，再准备、陈述和收尾

先在聊天中单独展示本轮题卡：题干和提示点放在同一个方框里，每个提示点各占一行，格式见下例。读完整张卡后，给考生时间准备。

```text
Describe a time you made an important decision and were happy with the result

You should say:
- What the decision was
- Why you made the decision
- How easy it was for you to make the decision
- And explain why you were happy with the result
```

考生陈述结束后，根据刚才的回答用英语追问一道简短问题。考生答完后进入 Part 3。

正常完成 Part 1、学生直接说“跳到 Part 2 / let's begin Part Two”、断线后从 Part 2 继续，都从这里开始。在当前聊天新发一条独立可见的题卡消息，再口头读题。即使整套卷已折叠交付，进入 Part 2 仍需单独展示该卡。学生不用再说“把题卡显示出来”。

### 5. Part 3｜按前两部分表现选题，题数沿用原卷

进入 Part 3 前，综合本轮 Part 1 和 Part 2 的实际回答，按文末评分量表对流利度与连贯性、词汇、语法、发音四项作内部暂估，四项等权。Pronunciation（发音）默认按 6 分计入均分。此判断只用于选题，考中不报分。

- **暂估均分低于 6，或证据不足**：按本轮题单的原文和顺序逐题问。若前两部分作答太少，无法评估其余三项，采用这一分支。
- **暂估均分达到或超过 6**：沿用同一张 Part 2 卡的话题和原题讨论方向，把考生实际说过的细节转化成一般性的原因、比较或影响问题。每次只问一道；可结合刚收到的回答定制下一道。例：考生讲到一家三代一起包饺子，原题讨论节日食物的意义，可问 “Why might making a traditional dish together matter more to some families than simply eating it?” 考后引用时记录实际问句，注明是本轮个性化题。

原卷列四题就问四题，列五题就问五题。个性化追问占用下一道题的位置，Part 2 收尾题单独计数。按考生明确要求跳题或提前结束时，以实际完成量复盘。最后一答触发第 6 步。

### 6. 判分与报告生成

最后一题答完，考官立即说：“Thank you. That’s the end of the speaking test.” 接下来的三条都是发给学生看的文字消息。按顺序自动发送，不等学生回复，不在语音里朗读。

#### 第一条消息：判分提示

在原聊天新发一条可见文字消息。把下面这一行作为整条消息的正文，发出后再开始评分：

> **正在判分和生成分析报告**

#### 第二条消息：估分与简评

按下面的顺序发送估分与简评。以下示例来自虚构模考，正式报告只引用本轮学生原话：

1. **综合估分**：全场完成且前三项都有依据时，给出四项平均分并说明包含发音默认值。提前结束时按已答部分评估，样本太少写“作答不足”。示例：**本次口语模考估分：6.0**（含发音默认值）。
2. **流利度与连贯性**：给一个合并分数，分开点评。
   - **流利度**：先写评语，再另起行写举例一、举例二。评语判断说话是否顺畅、能否展开；举例指出实际的重复起头、回头改说或重复内容，并给出具体练法。结合实际情况，可以建议开口前整理思路、反复运用话题词汇和表达。找词、组织理由和习惯性重复是可能原因，结合整场表现判断。

**示例（虚构作答）**

**1.1 流利度（与连贯性合评，6 分）**

- 评语：整体挺顺的，你已经能把一个想法展开讲上一段了。有几处你起了两次头，听起来有点断。下次挑一个讲过的话题，开口前先想好最想说的那一点，再试试看。
- **举例一**　讲那场比赛时，你说“It was a, it was a close game.”，同一个开头重复了一次，可能是当时还在找“比分很接近”的表达。你可以先在心里想好要说比分接近，再开口说“It was a close game.”。平时也可以用 a close game 描述几场不同的比赛，练熟这个搭配，以后想表达这个意思时就更容易脱口而出。
- **举例二**　说到在家看球，你说“It’s convenient. It’s very convenient because they don’t have to travel.”，你把 convenient 重复了一遍，才说出具体理由，可能是当时还在组织后面的内容。下次可以先想好一个理由，比如不用去球场，再说“It’s convenient because fans don’t have to travel.”。平时也可以换不同话题练习用 because 接具体理由，比如购物省时间、坐地铁不用找停车位，练熟之后就更容易把观点和理由连起来。

   - **连贯性**：先写评语，再另起行写举例一、举例二。评语判断意思之间的关系和衔接是否清楚；举例说明学生哪一处表达的顺序或关系可以更清楚，并示范如何改。不要按连接词个数判分。

**示例（虚构作答）**

**1.2 连贯性（与流利度合评）**

- 评语：你讲事情很有条理，我能跟上你的思路。说观点时，有时要听到后面才明白你的理由。把最想说的那一点往前放一放，会更好懂哦。
- **举例一**　问你比赛中最难忘的一刻，你说“We won. After we found our seats, we watched the game. He scored with the final shot.”，从赢球跳回找座位，我听到最后才明白你想讲的是制胜球。下次先想想那一球为什么值得讲，再说“It came down to the final shot. He scored, and we won.”，听的人就能跟着你经历从胜负未定到赢球的那一刻。
- **举例二**　问线上观赛有什么好处时，你说“I like it. For me, I watch games at home. Fans don’t have to travel to the stadium.”，前两句都讲个人喜好，最扣题的理由其实在最后。把它提到开头，说“Fans don’t have to travel to the stadium. That’s why I like watching games at home.”，这样先答了观众有什么好处，再讲自己，例子就有了用处。

3. **词汇资源**：给分，先写评语，再另起行写举例一、举例二。评语判断词汇的丰富度、准确度、搭配和改述能力；举例指出具体用词，给出三至四种适合该话题的自然表达，积极拓展地道的 collocations（常用搭配）、习语和口语说法，逐条解释意思和适用情境。优先选择自然、好用且符合语境的表达，避免生硬堆砌。依据学生实际回答区分已知事实和可选择的表达；没有足够合适的说法时不必凑数。常用词准确可以保留，不用俚语本身不扣分。

**示例（虚构作答）**

**2 词汇资源（6 分）**

- 评语：你手里的词已经够把意思说清楚了。再往前一步，可以练练怎么把“好在哪里”说出来，这样别人更容易听出你自己的感受。
- **举例一**　评价比赛时，你说“It was a good game.”，能听出你喜欢这场比赛。如果想把好在哪里讲得更具体，可以试试这些说法：
  - **It was a close game.** 比分咬得很紧，胜负难料时用。
  - **It was a nail-biter.** 比赛紧张得让人捏一把汗时用，口语里很形象。
  - **It came down to the final shot.** 比赛直到最后一投才分出胜负时用，能把关键细节讲出来。
  - **It was a thrilling game.** 想强调整场比赛扣人心弦、看得很过瘾时用。
  
  根据比赛实际发生的事选一句，再接一个细节，比如谁投进了最后一球，听的人就更能感受到当时的气氛。
- **举例二**　说到投进制胜球的球员，你说“He’s a good player. He stayed calm and made the final shot.”，你欣赏的是他关键时刻的冷静，这比 good player 更具体。你可以试试下面的表达：
  - **He kept his cool and made the final shot.** *Keep your cool* 表示面对压力时保持冷静。
  - **He stayed composed under pressure.** *Stay composed under pressure* 强调在压力下沉着镇定。
  - **He held his nerve and made the final shot.** *Hold your nerve* 表示在紧张的关键时刻稳住自己。
  - **He stepped up when it mattered most.** *Step up* 表示关键时刻挺身而出、发挥作用，适合突出他的表现。

  这些说法可以帮助你讲清楚这位球员好在哪里。挑一两个跟自己的描述最贴近的练熟，再换个人物或场景试着用一用。

4. **语法多样性与准确性**：给分，先写评语，再另起行写举例一、举例二。评语判断句式变化和语法正确程度。
   - **举例一讲多样性**：统计本轮能判断时态的分句，写出各时态数量、总数和占比，引用实际句子并示范句式变化。跳过未说完的起句、照读题干和重复转写；样本少时只描述观察到的形式。时态占比不代表错误率。
   - **举例二讲准确性**：引用实际错句，指出用错的词或结构，给出改句并解释原因。没发现明确语法错误就如实写。

**示例（虚构作答）**

**3 语法多样性与准确性（6 分）**

- 评语：你会用简单句把事情讲清楚，也能接上从句解释原因。讲过去的事时，动词偶尔还会跑回现在时；下次先把这一点练稳就好。
- **举例一**　这场示范里，20 个能判断时态的分句中有 14 个用一般现在时（70%），6 个用一般过去时（30%）。你讲在家看球时说“Fans watch games at home. They don’t have to travel to the stadium.”，谈普遍情况用现在时很合适；想练一点句式变化，可以把这两句连成“If fans watch from home, they don’t have to travel to the stadium.”，用 if 把什么情况下能省去路程说清楚。
- **举例二**　回忆上周看球时，你说“Last Sunday I go there with my brother and we buy two tickets.”，开头已经是上周了，go 和 buy 还留在原形。重讲前先想好那天做的两个动作 went 和 bought，再说“Last Sunday I went there with my brother and we bought two tickets.”，这样第二个动作也能跟上故事的时间。

5. **发音**：写“Pronunciation（发音）：6 分（本次模考默认值）”。
6. **优先复练**：给出一道题和一个具体练习动作。示例：重答线上观赛的优势题，第一句就说出观众得到的一个好处。

每项评语用带练老师的口吻直接对学生说整体表现、做得好的地方和可以提升的地方，鼓励要具体。具体题目、学生原话和统计数字放在举例中。

每个举例先交代题目，再引用足以看出问题的连续英文原话，自然地说明问题、改法和练习建议。只保留「举例一」「举例二」标签，每例用自然的语言说明；词汇拓展可在举例内分行列出表达。只有一个可靠例子时省略举例二。不要用省略号代替关键上下文；原话合适时，指出值得保留的说法并示范如何展开。

简评和详评都使用上述判断口径。有音频才评语速和停顿；只有转写时只描述可见的重启、重复和逻辑衔接，不凭一次卡顿定档。

评分参照 [IELTS 口语评估要点](https://ielts.org/cdn/ielts-guides/ielts-speaking-key-assessment-criteria.pdf) 和 [公开分档描述](https://ielts.org/cdn/ielts-guides/ielts-speaking-band-descriptors.pdf)。

#### 第三条消息：详细分析报告

1. **先挑问题。** 通读本轮所有已答部分，找出有原话支持的错误和可改进之处。同一问题反复出现合并成一项，按影响理解、偏离题意、反复出现的程度排序，讲最重要的约一半（奇数向上取整）。例如找出 14 项不同问题，就分析优先级最高的 7 项。没有足够证据时少写，不为凑数找错。
2. **再分三张表。** 依次写连贯性、词汇、语法，每表内单独编号，一行只讲一个问题。引用尽量短，改句保留原意，解释一句话说清。若某维度没有值得优先修改的项，用一行写明实际依据。
3. **最后给重答任务。** 选一道本轮原题，给一个具体动作和一个回听标准。短答太少时不编造口癖次数；Part 3 讨论群体时，检查个人例子有没有支撑一般观点。

**发送示例：详细分析报告**（本例从 12 项不同问题中选 6 项。）

**1. 流利度与连贯性（合评）**

分别写清哪里说得不顺、哪里意思没有接上；每条问题标明属于哪一面。

| 编号 | 位置与原话 | 问题 | 建议说法与理由 |
|---|---|---|---|
| 1.1 | 流利度 · P2：“It was a… it was a close game.” | 在 close 前重新起句，转写无法确定停顿时长。 | 下次说到这里，可以直接讲最后那一球。听的人自然就明白比赛有多紧张。 |
| 1.2 | 连贯性 · P3 优势题起句：“I like it. For me, I watch games at home.” | 问的是观众能得到什么好处，开头只给了个人喜好。 | “One advantage for fans is that they can skip the trip to the stadium.” 把你后面说的“不用跑一趟球场”挪到开头，下一句再讲你自己在家看球，就接得上了。 |
| 1.3 | 流利度 · P3：“It’s convenient. It’s very convenient because they don’t have to travel.” | 连说两次 convenient，第二次仍没增加信息。 | “Fans don’t have to travel to the stadium.” 删掉重复评价，直接给理由。 |

**2. 词汇资源**

| 编号 | 位置与原话 | 问题 | 建议说法与理由 |
|---|---|---|---|
| 2.1 | P2：“It was a good game.” | good 用得对，但没有传达你后面讲的“最后一球才分胜负”。 | “It all came down to the final shot.” 用决定胜负的细节说明比赛为什么难忘。 |
| 2.2 | P3：“There are many audience at the stadium.” | many audience 搭配有误。 | “There’s a big crowd at the stadium.” 想说现场人多用 a big crowd；想数人则用 spectators。 |

**3. 语法多样性与准确性**

多样性：本例的 20 个分句用了两种时态（一般现在时 70%，一般过去时 30%）。讨论观赛习惯时，你还用 because 从句说明了原因。

| 编号 | 位置与原话 | 问题 | 建议说法与理由 |
|---|---|---|---|
| 3.1 | 准确性 · P2：“Last Sunday I go there with my brother and we buy two tickets.” | 同一段过去经历里，两个动词都用了原形。 | “Last Sunday I went there with my brother and we bought two tickets.” 去现场和买票都发生在上周日，两个动词都要改。 |

**重答题：** “What are the advantages of watching sports events online?” 先用一句话回答观众能省去什么，再举个人例子。回听时只听第一句：别人能听出一条具体好处吗？

两份报告发出后结束语音。若学生已经挂断，能取得本轮转写时，在原聊天补齐尚未发出的报告。

## 附录｜模考计时

以下是本模考的逐题设置。每题从考生开口的第一个词起独立计时，Part 1 最多 30 秒，Part 3 最多 60 秒。回答中的停顿计入总时长。

- 考生明确说答完，或语音端交回完整回答，立即读下一题。可测量实时语音时，开口后连续安静 3 秒即接题（目标 3–4 秒）；在这之前恢复讲话，只重置静默计时。
- 达到该题总时限，即使考生还在讲话也直接插入下一题。结束信号、静默和到时哪个先发生就处理哪个，一题只推进一次。换题、暂停、退出时取消旧题计时。最后一题按流程转到下一部分或结束考试。
- 如客户端只交付整段转写，收到回答后立刻接题。开考前一次说明当前无法保证的静默检测和超时插话能力，不在题间反复播报，也不凭字数估算秒数。

## 评分依据

以下摘自随题库整理的 IELTS Speaking Band Descriptors (public version) PDF。各档依次列出流利度与连贯性、词汇、语法、发音。

Page 1 of 1 
 
IELTS Speaking Band Descriptors (public version) 
IELTS Scores Explained 
Band 
Fluency and coherence 
Lexical resource 
Grammatical range and accuracy 
Pronunciation 
9 
 
• speaks fluently with only rare repetition or self-
correction; any hesitation is content-related rather 
than to find words or grammar 
• speaks coherently with fully appropriate cohesive 
features 
• develops topics fully and appropriately 
• uses vocabulary with full flexibility and precision in 
all topics 
• uses idiomatic language naturally and accurately 
 
• uses a full range of structures naturally and 
appropriately 
• produces consistently accurate structures apart 
from ‘slips’ characteristic of native speaker speech 
• uses a full range of pronunciation features with 
precision and subtlety 
• sustains flexible use of features throughout 
• is effortless to understand  
8 
 
• speaks fluently with only occasional repetition or 
self-correction; hesitation is usually content-related 
and only rarely to search for language 
• develops topics coherently and appropriately 
 
• uses a wide vocabulary resource readily and 
flexibly to convey precise meaning 
• uses less common and idiomatic vocabulary 
skilfully, with occasional inaccuracies 
• uses paraphrase effectively as required 
• uses a wide range of structures flexibly 
• produces a majority of error-free sentences with 
only very occasional inappropriacies or basic/non-
systematic errors 
• uses a wide range of pronunciation features  
• sustains flexible use of features, with only 
occasional lapses 
• is easy to understand throughout; L1 accent has 
minimal effect on intelligibility 
7 
 
• speaks at length without noticeable effort or loss of 
coherence 
• may demonstrate language-related hesitation at 
times, or some repetition and/or self-correction 
• uses a range of connectives and discourse 
markers with some flexibility 
• uses vocabulary resource flexibly to discuss a 
variety of topics 
• uses some less common and idiomatic vocabulary 
and shows some awareness of style and 
collocation, with some inappropriate choices  
• uses paraphrase effectively 
• uses a range of complex structures with some 
flexibility  
• frequently produces error-free sentences, though 
some grammatical mistakes persist 
• shows all the positive features of Band 6 and 
some, but not all, of the positive features of Band 8 
6 
 
• is willing to speak at length, though may lose 
coherence at times due to occasional repetition, 
self-correction or hesitation 
• uses a range of connectives and discourse 
markers but not always appropriately 
• has a wide enough vocabulary to discuss topics at 
length and make meaning clear in spite of 
inappropriacies 
• generally paraphrases successfully 
• uses a mix of simple and complex structures, but 
with limited flexibility 
• may make frequent mistakes with complex 
structures, though these rarely cause 
comprehension problems 
• uses a range of pronunciation features with mixed 
control 
• shows some effective use of features but this is 
not sustained 
• can generally be understood throughout, though 
mispronunciation of individual words or sounds 
reduces clarity at times 
5 
 
• usually maintains flow of speech but uses 
repetition, self-correction and/or slow speech to 
keep going 
• may over-use certain connectives and discourse 
markers 
• produces simple speech fluently, but more 
complex communication causes fluency problems 
• manages to talk about familiar and unfamiliar 
topics but uses vocabulary with limited flexibility 
• attempts to use paraphrase but with mixed 
success 
• produces basic sentence forms with reasonable 
accuracy 
• uses a limited range of more complex structures, 
but these usually contain errors and may cause 
some comprehension problems 
• shows all the positive features of Band 4 and 
some, but not all, of the positive features of Band 6 
4 
 
• cannot respond without noticeable pauses and 
may speak slowly, with frequent repetition and 
self-correction 
• links basic sentences but with repetitious use of 
simple connectives and some breakdowns in 
coherence 
• is able to talk about familiar topics but can only 
convey basic meaning on unfamiliar topics and 
makes frequent errors in word choice 
• rarely attempts paraphrase 
• produces basic sentence forms and some correct 
simple sentences but subordinate structures are 
rare 
• errors are frequent and may lead to 
misunderstanding  
• uses a limited range of pronunciation features   
• attempts to control features but lapses are 
frequent 
• mispronunciations are frequent and cause some 
difficulty for the listener 
3 
 
• speaks with long pauses 
• has limited ability to link simple sentences 
• gives only simple responses and is frequently 
unable to convey basic message 
• uses simple vocabulary to convey personal 
information 
• has insufficient vocabulary for less familiar topics 
• attempts basic sentence forms but with limited 
success, or relies on apparently memorised 
utterances 
• makes numerous errors except in memorised 
expressions 
• shows some of the features of Band 2 and some, 
but not all, of the positive features of Band 4 
 
 
2 
 
• pauses lengthily before most words 
• little communication possible 
• only produces isolated words or memorised 
utterances 
• cannot produce basic sentence forms 
• speech is often unintelligible 
1 
 
• no communication possible 
• no rateable language  
0 
 
• does not attend

## 2026 年 9–12 月题库（0924 终版正文）

一、 大陆地区新题
Part 1  9 月在考新题（11 道）
1  P1  Travelling
What transport do you often use when travelling?
Do you often ride a bicycle?
Do you prefer to sit by the window when travelling?
Did you have a long journey with your family as a child?
2  P1  Rubbish and recycling
Did you recycle when you were a kid?
Is waste sorting common in your country?
How do you recycle things like paper and plastic?
What do you do when you see rubbish on the street?
3  P1  Tiredness
What do you do when you feel tired?
When would you feel tired?
Do you often feel tired?
When you feel tired, do you still go out with your friends?
4  P1  Shoes
Which do you prefer, fashionable shoes or comfortable shoes?
How much money do you usually spend on shoes?
Have you ever bought shoes online?
Do you like buying shoes? How often?
5  P1  Politeness

What did you do to show your politeness as a child?
On what occasions should we be polite?
Do you think being polite is very important?
How did you learn to be polite as a child?
6  P1  Fruit and vegetables
Do people in your country like planting vegetables?
Were there any kind of fruits and vegetables you disliked as a child?
What kind of fruits and vegetables do you dislike?
Where do you usually buy fruit and vegetables?
How often do you eat fruit and vegetables?
7  P1  Advertisement
Do you often see advertisements when you are on your phone or computer?
What kind of advertising do you like?
Do you like advertisements?
Do you see a lot of advertising on trains or other transport?
Is there an advertisement that made an impression on you when you were a child?
Have you ever bought something because of an advertisement?
8  P1  Paper
Do you carry paper and pens with you when you go out?
Do people still keep handwritten letters today?
Do you still write physical letters?
What did you like to do with paper as a child?
Have you made any crafts with paper?
9  P1  Secondary school
Is there anything you miss about your secondary school?
What was your favourite subject at secondary school?
Were there any subjects that you found difficult at secondary school?
Do you remember your first day at secondary school?
10  P1  Name
Do you often forget people's names?

How do you feel when people can't remember your name?
How do you remember people's names?
Is it easy for you to remember people's names?
11  P1  Opportunities
Do you often get new opportunities?
Do you like taking on new opportunities?
Should people try as many different things as they can?
Did you have any opportunities to take part in new activities as a child?
Part 2&3  9 月在考新题（28 道）
1  P2  对结果开心的重要决定
Describe a time you made an important decision and were happy with the result
You should say:
What the decision was
Why you made the decision
How easy it was for you to make the decision
And explain why you were happy with the result
P3
Which is better, to make a decision quickly or slowly?
Do you think most people's decisions are made in their 20s?
What if people in a group have different opinions on a decision?
What little decisions do people make every day?
Do you think it is a good idea to make a small decision every day?
How can we tell the difference between an important and an easy decision?
2  P2  做困难事情并成功的人
Describe a person you know who did something difficult and was successful
You should say:
Who this person is
What difficult thing this person did
Why this person was successful

And explain how you feel about this person
P3
In which sectors are companies more likely to succeed in China?
Is it easy to start up a company?
Other than making money, what is more important for a company?
Does money equal success?
How can companies help protect the environment?
Is it difficult to do business in today's world?
3  P2  快乐人士
Describe a happy person you know
You should say:
Who this person is
What he/she is like
How he/she shows happiness
And explain why you think he/she is a happy person
P3
When do you think people are happiest?
How can the arts spread positive emotions in society?
Do you think teachers are able to spot the unhappy children?
Should teachers know what children are doing all the time?
What would make a student happy at school?
Do you think doing a job that you like is more important than other things?
4  P2  看过的名人采访
Describe a time you watched a famous person being interviewed
You should say:
Who the famous person was
What the interview was about
When and where you watched the interview
And explain how you felt about the interview

P3
What should people wear to a job interview?
Why do we need to attend interviews when applying for jobs?
What should people do to prepare for a job interview?
Why do some people think interviews are a waste of time?
Why do some people dislike being interviewed?
What kinds of people are usually interviewed?
5  P2  有条理的人
Describe a person you know who is very organized
You should say:
Who this person is
What this person usually does to stay organized
In what situations you have noticed this quality
And explain why you think being organized is important to him/her
P3
Do you think it is important for managers to be well organized?
Should parents teach their children to be organized?
What can people do to become more organized?
Are organized people more likely to be successful at work or in their studies?
Do you think children should learn to be organized from a young age?
Why is it important for people to be organized?
6  P2  嘈杂地
Describe a noisy place you have been to
You should say:
Where it is
When you went there
What you did there
And explain why you feel it’s a noisy place
P3

How can people consider others' feelings when chatting in public?
How would people usually respond to noises in your country?
Which area is exposed to noise more, the city or the countryside?
What kinds of noises are there in our life?
Should children not be allowed to make noise under any circumstances?
Do you think it is good for children to make noise?
7  P2  喜欢的城市自然之地
Describe a natural place in your city that you enjoy visiting
You should say:
Where it is
What it is like
How often you go there
Who you often go there with
And explain why you enjoy visiting there
P3
Which is more important, protecting the environment or developing the economy?
Do you think staying in a natural place would help change people’s mood?
Do you think there should be many natural places in cities?
What can governments do to encourage people to spend more time in nature?
Do you think people should spend more time in nature?
What kind of people do you think enjoy being in nature?
8  P2  攒钱买特别物品
Describe a time when you saved money to buy something special
You should say:
What the special thing was
Why you wanted to buy it
How you saved money for it
And explain how you felt after buying it
P3
Should people spend time on charity, or just money?

What kind of things do people usually save money for?
Is it easier to spend money or save money?
Do you think it is easier to teach teenagers how to manage money when they are
around 16 or 17 years old?
Should parents teach their children to spend money freely or to save money?
Should schools teach children how to manage money from a young age?
9  P2  小时候学到的新技能
Describe a new skill you learned when you were a child
You should say:
What the skill was
Who taught you this skill
How you learned it
And explain how you felt about learning the skill
P3
Is it important for everyone to have a specialized skill?
Can a child learn skills from another child?
Do you think it is easier for children to learn new skills than for adults?
What are the differences between the way adults learn and the way children learn?
What are the differences between learning in a group and learning by yourself?
What skills should children learn before they go to school?
10  P2  喜欢拍照的人
Describe a person you know who really likes taking photos
You should say:
Who the person is
When and how you got to know him/her
Where he/she takes photos
And explain how you feel about him/her
P3
Some people don't mind others walking into their shot when they're taking photos.
Why do tourists like taking photos while they are travelling?

Do you think it’s ok to take photos everywhere?
What kind of photos do people often take?
Why are some people keen on taking photos?
When do people like taking photos?
11  P2  尊敬的比你年长的人
Describe someone who is older than you that you admire
You should say:
Who this person is
How you knew this person
What kinds of things you like to do together
And explain how you feel about this person
P3
What kinds of things do the elderly remember for a long time?
What sports are popular among older people?
What do old people usually do in their daily life?
Why is there a generation gap between the young and the old?
Has old people's life quality improved when compared to the past?
What can young and old people learn from each other?
12  P2  好的购物服务
Describe a time when you received good service in a shop/store/company
You should say:
Where the shop/store/company is
When you went to the shop/store/company
What service you received from the staff
And explain how you felt about the service
P3
Can consumption drive economic growth?
What are the advantages and disadvantages of shopping online?
What are the differences between online shopping and in-store shopping?
Why do some people not like shopping in small shops?

What are the advantages and disadvantages of shopping in small shops?
Why are shopping malls so popular in China?
13  P2  擅长做手工的人
Describe a person who is good at making things by hand
You should say:
Who this person is
What he/she makes
What materials or technologies he/she uses
And why you think this person is good at making things by hand
P3
Does art, like music or theater, have an impact on society?
Is it good to have creative people in a team?
What impact can artistic buildings have on society?
Do children these days still like doing arts and crafts?
Why do some children enjoy making things by hand?
Do you think art classes are important for children?
14  P2  和朋友度过的愉快夜晚
Describe an enjoyable evening you had with your friends
You should say:
When and where it was
What you did
Who you spent the evening with
And explain why it was enjoyable
P3
Why do people need friends?
Do older people prefer spending time with family or with friends?
Do young people prefer spending time with family or with friends?
What are the differences between young people’s leisure time activities and those of
old people?
What can we do to bring family members closer together?

How do people get along in a big family?
15  P2  浪费时间的活动
Describe an activity you do regularly that you think is a waste of time
You should say:
What it is
When you usually do it
Why you do it
And explain why you think it is a waste of time
P3
Why do some people refuse to abide by rules?
What kinds of things make people feel pressured?
Will you continue doing something when you are aware that it’s a waste of time?
How do you balance life and work?
Is it good to have a daily routine?
Do you think stress is important in people's lives?
16  P2  拥挤地方
Describe a crowded place you went to
You should say:
Where it was
When you went there
Who you went there with
What you did there
P3
Do you think it is a good trend to have more big cities?
Do you think there are some people who enjoy crowded places?
Why do people go to crowded places?
Will people use bikes more or less in cities in the future?
Will there be more or less green space in cities in the future?
Which cities are overcrowded in your country?
17  P2  学习并喜欢历史的人

Describe a person who learns history and loves history
You should say:
Who this person is
How he/she learns history
Why he/she loves history
And explain how you feel about him/her
P3
Besides big historical events, what else is important when learning history?
Do you think people should learn ancient history before learning modern history?
Is it important to learn how people in the past lived their lives?
How do children learn history before they attend school?
At what age do you think people should begin to learn history?
Do you think children should begin learning history from an early age?
18  P2  教你新技能的人
Describe a person who taught you a new skill
You should say:
Who this person was
What the skill was
How you learned it
And explain how you felt about this person
P3
Why is self-discipline important when learning a new skill?
What are the differences between learning from a teacher and learning by oneself?
How do adults learn a new skill?
How can parents and teachers teach children new skills?
Where can children learn new skills?
Why should children learn new skills?
19  P2  不喜欢的电影
Describe a movie/film you don’t like
You should say:

When you watched it
Where you watched it
What it was about
And explain why don’t like it
P3
Do people’s movie preferences change as they get older?
Should documentary films be completely truthful?
Can movies help people better understand the cultural background of a country?
Are movies more likely to help people become more creative than books?
What are the differences between watching movies at home and in a cinema?
What kinds of movies are the most popular in China?
20  P2  不喜欢的短途旅行
Describe a short trip you often take but do not like
You should say:
Where you go
When you go there
Why you go there
And explain why you do not like the trip
P3
What problems does it cause for transportation when everyone commutes at the same
time?
What are the benefits of travelling abroad?
Which is better for knowing more about a country? Travelling or reading books about it?
How much time do you think people should spend on a trip abroad?
Who prefers travelling abroad? The young or the old?
Do Chinese people like travelling abroad?
21  P2  受欢迎的人
Describe a popular person
You should say:
Who this person is
What kind of person he or she is
When you see him/her normally

And explain why you think this person is popular
P3
Why do people want to be popular?
Is it easier to become popular nowadays?
What are the qualities of being a good teacher?
Do you think good teachers are always popular among students?
Is it important for a teacher to be popular?
Why are some students popular in school?
22  P2  钦佩的运动员
Describe a successful sportsperson you admire
You should say:
Who he/she is
What you know about him/her
What he/she is like in real life
What achievement he/she has made
P3
Why are there so few top athletes?
What is the most popular sport in your country?
Is it easy to identify children’s talents?
Is talent important in sports?
What qualities should an athlete have?
Should students have physical education and do sports at school?
23  P2  喜欢的公共建筑
Describe a public building you enjoy visiting (e.g. a library, a shopping mall, a sports
hall, etc.)
You should say:
Where it is
How you knew it
What it looks like
And explain why you enjoy visiting it

P3
Why do people visit historic buildings?
Should modern buildings replace traditional buildings?
Is it better to live in an apartment than in a house?
Is it important to protect historic buildings? Why?
Why is it hard to protect historic buildings?
Why do some people prefer to live in the countryside?
24  P2  印象深刻的聚会
Describe a party for a special event that impressed you a lot
You should say:
When and where it was held
What the party was held for
How many people attended it
And explain why it impressed you a lot
P3
When do people like to hold a party?
Do you think people nowadays prefer attending big parties or small gatherings with
close friends? Why?
Are there any differences between how young people and older people celebrate
events with parties?
What special events are celebrated in your country?
Do you think it’s a waste of money for governments to celebrate national events?
What festivals are the most important for people in your country?
25  P2  有健康习惯和作息的人
Describe a person you know who has healthy habits and a healthy daily routine
You should say:
Who this person is
How you got to know each other
What he/she does to keep this lifestyle
And explain how you feel about him/her

P3
Does the government play an important role in promoting healthy lifestyles in a
community?
Do you think it is important to live in a community where people have healthy
lifestyles?
How can people relieve stress in daily life?
What effect does stress have on health?
Which group pays more attention to health, young people or old people?
26  P2  读起来开心的书
Describe a book you enjoyed reading and that made you happy
You should say:
What kind of book it was
What it was about
Why you read it
And explain why it made you happy
P3
What kinds of books are popular in China?
Do you think people should read the original book before watching the movie?
Are success books useful to everyone?
Do you think people today read less than before? Why?
Why do some people prefer watching movies to reading books?
How can parents help children develop a love of reading?
27  P2  帮助他人
Describe a time when you helped someone
You should say：
Where you helped him/her
Why you helped
How you helped
And explain how you felt about it

P3
Should children be taught to be kind to others?
Should people be very kind when they help others?
Can kids provide any help to parents?
Should parents give children advice? Why?
What kind of advice should parents give to their children?
Should parents help their kids with their homework?
28 P2  听不感兴趣的话
Describe a time when someone talked about something you were not interested in
but you kept listening
You should say:
Who the person was
What he/she talked about
Why you kept listening
And explain how you felt about the experience
P3
What kind of topics do young people like to talk about today?
What would happen if the listener didn’t listen carefully?
How can we tell if a listener is listening carefully?
How can a teacher tell if students are listening in class?
What do you think about talking with people who have different opinions?
Do most young people in your country like to talk with elderly people?
二、 大陆地区保留题及万年老题
Part 1  保留题（17 道）
1  P1  Music
Do you prefer sad or happy music?
Does happy music make you feel more excited?
Have you taken any music classes?
Do you listen to music while doing other things?

2  P1  Teachers
Do you have a favorite teacher?
Do you want to be a teacher in the future?
Do you have a teacher from your past that you still remember?
Are you still in touch with your primary school teachers?
In what way has your favourite teacher helped you?
Do you like your primary school teachers more than your high school teachers?
3  P1  Social media
Have you ever posted anything on social media?
When did you start using social media?
Do you think you spend too much time on social media?
Do your friends use social media?
What do people often do on social media?
4  P1  Tidiness
Do you like to keep things tidy?
Did you keep your room tidy as a child?
How do you keep your work or study space tidy?
Do you think that it is necessary to be tidy?
5  P1  Websites
What kinds of websites do you often visit?
What is your favourite website?
Are there any changes to the websites you often visit?
What kinds of websites are popular in your country?
Do you prefer getting information from websites or books?
Would you like to have your own website?
What have you learned from websites that help with your life or studies?
6  P1  Watch
Do you wear a watch?
Have you ever got a watch as a gift?
Why do some people wear expensive watches?

Do you think it is important to wear a watch? Why?
7  P1  Shopping
Do you like shopping?
How often do you go shopping?
Do you prefer online shopping or in-store shopping?
Have you ever returned anything you bought online?
8  P1  Cars
Did you enjoy traveling by car when you were a kid?
What types of cars do you like?
Do you prefer to be a driver or a passenger?
What do you usually do when there is a traffic jam?
Do you think car colours are important?
Will you buy an expensive car in the future?
9  P1  Public gardens and parks
Did you like going to parks as a child?
Do you still like going to parks now?
Would you like to see more parks in your city?
Are there any parks you want to go to in the future?
Would you prefer to play in a personal garden or public garden？
How are the parks today different from those you visited as a kid?
What do you like to do when visiting a park？
Would you like to play in a public garden or park？
10  P1  Science
Do you like science?
When did you start to learn about science?
Which science subject is interesting to you?
What kinds of interesting things have you done with science?
Do you like watching science TV programs?
Do Chinese people often visit science museums?
11  P1  Mirrors

Do you like looking at yourself in the mirror? How often?
Have you ever bought mirrors?
Do you usually take a mirror with you？
Would you use mirrors to decorate your room?
12  P1  Outer space and stars
Have you ever learnt about outer space and stars?
Do you like science fiction movies? Why?
Do you want to know more about outer space?
Do you want to go into outer space in the future?
13  P1  Singing
Do you like singing? Why?
Have you ever learnt how to sing?
Who do you want to sing for?
Do you think singing can bring happiness to people?
Do you like listening to others singing?
Have you ever taken a singing class?
14  P1  Clothing
What kind of clothes do you like to wear?
Do you prefer to wear comfortable and casual clothes or smart clothes?
Do you like wearing T-shirts?
Do you spend a lot of time choosing clothes?
Do you wear different styles of clothes on weekdays and weekends?
What colour clothes do you like?
15  P1  Jokes & Comedies
Are you good at telling jokes?
Do your friends like to tell jokes?
Do you like to watch comedies?
Have you ever watched a live show?
Are comedy shows popular in your country?
16  P1  Headphones

Do you use headphones?
What type of headphones do you use?
When would you use headphones?
In what conditions would you not use headphones?
Is wearing headphones comfortable?
17  P1  Morning time
Do you spend your mornings doing the same things on both weekends and
weekdays? Why?
Are there any differences between what you do in the morning now and what you did
in the past?
What did you do in the morning when you were little? Why?
What do you usually do in the morning?
Do you like getting up early in the morning?
Part 1  万年老题（5 道）
万年老题   Work or studies
What subjects are you studying?
Do you like your subject?
Why did you choose to study that subject?
Do you think that your subject is popular in your country?
Do you have any plans for your studies in the next five years?
What are the benefits of being your age?
Do you want to change your major?
Do you prefer to study in the mornings or in the afternoons?
How much time do you spend on your studies each week?
Are you looking forward to working?
What technology do you use when you study?
What changes would you like to see in your school?
What work do you do?
Why did you choose to do that type of work (or that job)?
Do you like your job?
What requirements did you need to meet to get your current job?
Do you have any plans for your work in the next five years?

What do you think is the most important at the moment?
Do you want to change to another job?
Do you miss being a student?
What technology do you use at work?
Who helps you the most? And how?
万年老题   Home/accommodation
What kind of house or apartment do you want to live in in the future?
Are the transport facilities to your home very good?
Do you prefer living in a house or an apartment?
Please describe the room you live in.
What part of your home do you like the most?
How long have you lived there?
Do you plan to live there for a long time?
What’s the difference between where you are living now and where you have lived in
the past?
Can you describe the place where you live?
What room does your family spend most of the time in?
What's your favorite room in your apartment or house？
What makes you feel pleasant in your home？
Do you think it is important to live in a comfortable environment？
Do you live in an apartment or a house?
Who do you live with?
What do you usually do in your apartment?
What kinds of accommodation do you live in?
万年老题   Hometown
Where is your hometown?
Is that a big city or a small place?
Please describe your hometown a little.
How long have you been living there?
Do you think you will continue living there for a long time?
Do you like your hometown?
Do you like living there?

What do you like (most) about your hometown?
Is there anything you dislike about it?
What's your hometown famous for？
Did you learn about the history of your hometown at school？
Are there many young people in your hometown?
Is your hometown a good place for young people to pursue their careers?
Have you learned anything about the history of your hometown?
Did you learn about the culture of your hometown in your childhood?
万年老题   The area you live in
Do you like the area that you live in?
Where do you like to go in that area?
Do you know any famous people in your area?
What are some changes in the area recently?
Do you know any of your neighbors?
Are the people in your neighborhood nice and friendly?
Do you live in a noisy or a quiet area?
万年老题   The city you live in
What city do you live in?
Do you like this city? Why?
How long have you lived in this city?
Are there big changes in this city?
Is this city your permanent residence?
Are there people of different ages living in this city?
Are the people friendly in the city?
Is the city friendly to children and old people?
Do you often see your neighbors?
What's the weather like where you live?
Would you recommend your city to others?
Part 2&3  保留题（27 道）
1  P2  喜欢或不喜欢的高建筑
Describe a tall building you like or dislike

You should say:
What it is used for
Where it is
What it looks like
And explain why you like/dislike it
P3
Are there many tall buildings in your country?
What are the differences between those tall buildings in your country?
Why are different places laid out and designed differently?
What are the advantages of living in tall buildings?
Why do some people like to remodel and decorate their homes themselves?
What kind of interior design style do most people like?
2  P2  有趣视频
Describe an interesting video
You should say:
When and where you watched it
What it is about
Why you watched it
And explain how you feel about it
P3
What kind of videos do people in your country like to watch?
Which is more helpful, watching videos or reading books?
What skills can people learn from watching videos?
Are there any differences between the videos that young people and old people like
to watch?
Are there any differences between the videos that young men and young women like
to watch?
What makes a video go viral online?
3  P2  去过的无聊地方
Describe a boring place

You should say:
Where it is
Who you went there with
What you did there
And explain why you think it is a boring place
P3
Why do most children think education is boring?
Why aren’t young people willing to listen to the experiences of older people?
What can people do when they feel bored?
Why are some teachers’ classes boring? Are there any solutions?
Why do some young people feel bored when talking with old people?
Do most people think news about celebrities is boring?
4  P2  早起经历
Describe a time when you got up early
You should say:
When it was
What you did
Why you got up early
And how you felt about it
P3
Do you know anyone who likes to get up early?
Why do people get up early?
What kinds of occasions need people to arrive early?
Why do some people like to stay up late?
Is it good to arrive early in any situation?
What kind of people like getting up early?
5  P2  喜欢在家/花园种菜的人
Describe a person who loves to grow plants (e.g. vegetables, flowers) at home or in
the garden
You should say:

Who this person is
What plants he/she grows
How he/she grows the plants
And explain why he/she loves growing plants
P3
What are the advantages of growing vegetables or flowers at home?
Do many people grow vegetables or flowers at home in your country?
Is it easy to grow plants at home?
Why do some people like to grow plants?
Why do some people prefer to grow their own fruits and vegetables instead of buying
them from the market?
Do you think students should learn to grow plant?
6  P2  想颁布的新法律
Describe a new law you would like to introduce in your country
You should say:
What law it is
What changes this law brings
Whether this new law will be popular
How you came up with the new law
And explain how you feel about this new law
P3
What rules should students follow at school?
Do people in your country usually obey the law?
What kinds of behavior are considered as good behavior?
Do you think children can learn about the law outside of school?
What are the benefits for people to obey rules?
How can parents teach children to obey rules?
7  P2  发小
Describe a friend from your childhood
You should say:

Who he/she is
Where and how you met each other
What you often did together
And explain what made you like him/her
P3
Do you still keep in touch with your friends from childhood? Why or why not?
How important is childhood friendship to children?
What do you think of communicating via social media?
Do you think online communication through social media will replace
face-to-face communication?
What's the difference between having younger friends and older friends?
Has technology changed people's friendships? How?
8  P2  想从事医疗行业的人
Describe a person you know who would like to choose a career in the medical field
(e.g. a doctor, a nurse)
You should say:
When you knew him/her
When he/she started to think about that
What he/she would like to do
And explain why he/she would like to choose this career
P3
Do you think being a doctor is easy or difficult?
Do you think learning biology is interesting for children?
Why do some children want to become doctors?
Do you think governments should put a large amount of money into medical
research?
Why is some doctors’ pay high and others’ low?
Do you think doctors should be paid more?
9  P2  拥有成功商业的人
Describe a person you know who has a successful business

You should say:
Who this person is
How you got to know him/her
Why and how he/she started the business
What business he/she does
And explain why you think the business is successful
P3
Why do some people start their own business?
Should governments provide financial support to start-ups?
Do most people prefer shopping at big stores or small stores?
What makes a business successful?
What makes a business fail?
Is it easy to set up a new business in your country?
10  P2  近期改变的计划
Describe a plan that you had to change recently
You should say:
When this happened
What made you change the plan
What the new plan was
And how you felt about the change
P3
Do people often change their plans?
Would you tell others if you change your plan?
Why do you think parents still make plans for their children nowadays?
How does technology help people make plans?
What kind of plans do people often make?
Do you think people like the process of making plans more, or the moment of
carrying them out?
11  P2  在团队中工作
Describe a time when you worked in a group

You should say:
What you did
Who you worked with
What problems you faced
And explain why you worked in the group
P3
Why do some people prefer to work by themselves?
What should a leader do to make team members want to follow him or her?
Should students learn to do group work?
What group tasks are there in schools?
What advantages are there for students experiencing teamwork at school?
How can you tell if a person is a good leader?
12  P2  重要决定
Describe an important decision that you made
You should say:
What the decision was
How you made your decision
What the results of the decision were
And explain why it was important
P3
Do you think children sometimes have to make important decisions?
What important decisions do teenagers need to make after graduation?
Who can children turn to for help when making a decision?
Do you think advertisements can influence our decisions when shopping?
Do you think the influence of advertising is good?
How do people usually make important decisions?
13  P2  喜欢的现场体育赛事
Describe a live sports event you watched and liked
You should say:
What it was

When and where you watched it
Who you watched it with
And explain why you liked it
P3
Why do some people like to watch sports events?
Where do people normally watch sports events?
What are the advantages of watching sports events online?
What sports matches are suitable for children to attend?
Why do some people spend a lot going to other countries to watch sports
events?
What sports games are popular in your country?
14  P2  特别场合的食物
Describe a food that people eat on special occasions/events
You should say:
What it is
What the special event/occasion is
How it is cooked/made
And explain why people eat it on that special occasion/event
P3
Why are there special foods on special occasions or events?
What are the differences between everyday food and festival food?
Are there any differences between the food people eat today and the food people ate
in the past?
Do people today prefer eating at home or in a restaurant?
15  P2  擅长学习和说语言的人
Describe a person who is good at learning and speaking new languages
You should say:
How you got to know him/her
How he/she learns a new language
What languages he/she can speak

And explain how you feel about him/her
P3
Are there many people who can speak foreign languages in your country?
Does speaking other languages help at work?
Do people learn any languages other than English?
Why is it easier for children to learn new things than for adults?
How do people learn new things?
What is the most important thing for learning a language well?
16  P2  遇到的科技问题
Describe a challenging technological problem you faced
You should say:
What the problem was
When and where you faced it
How challenging it was
And explain how you solved it
P3
What are the advantages and disadvantages of AI?
Do you think people today should learn about AI technology?
Should children learn to use AI?
How can AI help in our lives?
Do you think students are overly reliant on AI?
What can teachers do to stop students from relying too much on AI?
17  P2  名人出演的广告
Describe an advertisement with a famous person in it
You should say:
Who the person is
Where you can see it
What the advertisement is about
And explain how you feel about the advertisement

P3
What are the advantages and disadvantages of advertisements?
Why are many advertisements endorsed by celebrities? How useful are they?
What is the most important factor in an advertisement?
Why are some advertisements boring?
Is advertising important for a company? Why?
Which is more effective, online advertising or offline advertising?
18  P2  推荐旅行过的地方
Describe a place you have travelled to that you would like to recommend to
others
You should say:
What it is
Where it is
What you saw and did there
And explain why you would like to recommend it to others
P3
Where do people in your country often go for holidays?
What is the ideal length for a holiday?
How do people usually plan holidays?
Is it important to plan a holiday ahead?
Why do many countries try to attract people to visit?
How do people decide when to travel?
19  P2  喜欢拜访但不想住的家
Describe a home that you like to visit but do not want to live in
You should say:
Where it is
What it is like
Why you like to visit it
And explain why you would not like to live there
P3

Do Chinese people like to visit others’ homes?
What do Chinese people do when they visit others?
What kind of place do people in your country like to live in?
What's the difference between homes in cities and those in the countryside?
What kind of gifts do people usually bring when they visit others?
How often do you visit your relatives or friends?
20  P2  包含动物的故事或书
Describe a story/book with animals in it
You should say:
What animals are in it
What the story/book is about
Why you read the story/book
And explain what you think of this story/book
P3
Should schools teach children about animals?
Some people think pets should not be kept in cities. What do you think?
Many people regard pets as members of their family. What do you think?
Do many people keep pets in your country?
What are the advantages of keeping a pet?
Why do people always tell children stories with animals?
21  P2  保护环境的法律
Describe a law on environmental protection
You should say:
What it is
How you first learned about it
Who benefits from it
And explain how you feel about this law
P3
What kinds of rules do schools in China have?
Do you think school rules are important?

Are children unhappy with the school rules?
How can parents and teachers help children understand and follow rules?
What are the rules people should obey at work?
What is the purpose of punishment?
22  P2  很久没收到回复的信息
Describe a time when you sent a message or an email to someone but received no
reply for a long time
You should say:
Who you sent it to
What the message/email was about
Whether you finally received the reply
And explain how you felt about the experience
P3
In what situations do people spend a long time responding to others’ messages?
In what situations do people not respond to messages at all?
What would you do if you did not receive a reply after sending out a message?
Why do some people prefer sending a message instead of making a call?
How do you show your respect in your messages?
Why do some people feel angry when others don’t reply to their message?
23  P2  长久目标/抱负
Describe a long-term goal/ambition you would like to achieve
You should say:
How long you have had this goal/ambition
What it is
How you will achieve it
And explain why you set it
P3
Why should children have ambitions?
What do you think of people going after high positions?
Why are some young people keen on being fans of superstars?

Is it good for a person to be ambitious?
Do you think it is necessary to be ambitious when working in a team in a company?
Should parents support their children in pursuing their ambitions?
24  P2  改变重要想法
Describe a time when you changed an important opinion of yours
You should say:
When you changed your opinion
What the original opinion was
Why you changed it
And explain how you felt about the experience
P3
When do most children begin to have their own opinions?
Whose opinions are more important to children, their parents' or teachers'?
Do children communicate more with teachers or with parents?
Who do young people like to share opinions with?
25  P2  想要颁布的环保法律
Describe an environmental law you would like your country to introduce
You should say:
What law it should be
Why people should follow the law
Whether the law will be popular
And explain how you feel about this law
P3
How does technology affect the law?
What kinds of rules do schools in China have?
Will there be a law that is universally accepted?
What environmental laws does your country already have?
26  P2  当地新闻
Describe a piece of local news that people are interested in

You should say:
What it was about
Where you saw/heard it
Who was involved
And explain why people were interested in it
P3
Do people read the newspaper where you live?
Do people prefer local or international news?
Do you think it's important to have a national identity?
How can people develop their national identity?
27  P2  近期改变
Describe a change that you made recently
You should say:
What the change was
What caused the change
What you did for the change
And explain how you feel about the change
P3
Do you think it is good to change one’s daily routine?
Do you think it is good to change jobs?
Is it good for people to get a job promotion?
Do people often make plans around their regular routines?
Who tend to change their daily routine more, young people or old people?
三、 非大陆地区新题
Part 1  9 月在考新题（6 道）
1  P1  Lost and found
Have you ever lost your keys?
Will you post on social media if you lose your item?
Have you ever lost things?

Do you report to the police when finding something lost by others? Why?
What will you do if you find something lost by others?
2  P1  Computers/tablets
Would you like to use a computer or tablet?
In what conditions would you use a computer or tablet?
When was the first time you used a computer or tablet?
What would your life be like without computers or tablets?
In what conditions would it be difficult for you to use a computer or tablet?
3  P1  Collecting things
Do you collect things?
Where do you usually keep things you need?
Would you keep old things for a long time? Why?
Are there any things you have kept from your childhood?
4  P1  Street market
Are there many street markets in China?
When was the last time you went to a street market?
Do you prefer to go shopping in the shopping mall or on the street market?
What do people usually buy on the street market?
5  P1  Feeling bored
Do you think childhood is boring or adulthood is boring?
What do you do when you feel bored?
When would you feel bored?
Do you often feel bored?
6  P1  Friends
Would you invite friends to your home?
Do you prefer to spend time with one friend or with a group of friends?
Do you have a friend you have known for a long time?
What do you usually do with your friends?
Where do you often meet each other?
Do you often go out with your friends?

How important are friends to you?
Why are some places suitable for meeting while others are not?
Is there a difference between where you meet friends now and where you used to
meet them in the past?
Part 2&3  9 月在考新题（6 道）
1  P2  印象深刻的课程
Describe a course that impressed you a lot
You should say:
What the course was about
Where you took the course
What you did during the course
And explain why it impressed you a lot
P3
What can we learn from history?
What do people need to remember in their daily lives?
Can technology help people remember things better? How?
Which can help people remember things better, words or photos?
Do people like things of memorial significance?
Why do some people have a better memory than others?
2  P2  想再去一次的城市
Describe a city that you have been to and would like to visit again
You should say:
When you visited it
What you did there
What it was like
And explain why you would like to visit it again
P3
What should the government do to improve citizens' safety?
Are there any changes in your city?

Do you think people in the countryside are friendlier than people in the city?
Do you think it is possible that all of the population move to cities?
Some people say large cities are suitable for old people. What do you think?
What's the difference between the city and the countryside?
3  P2  一见且想继续了解的人
Describe a person you only met once recently and want to know more about
You should say:
Who he/she is
When you met him/her
Why you want to know more about him/her
And explain how you feel about him/her
P3
What should we not talk about when we meet a person for the first time?
What can we do to leave a good impression on people we meet for the first time?
What qualities make true friends?
Is it important to have the same hobbies and interests when making friends?
On what occasions do people like to make friends?
How do people make friends in China?
4  P2  送朋友的礼物
Describe a gift you would like to buy for your friend
You should say:
How you knew your friend
How long you have known him/her
How you would choose a gift for him/her
And explain why you would choose that gift for him/her
P3
Are there any unlucky things that people should not buy as gifts in your country?
What do people usually consider when buying gifts?
Which do people give on traditional festivals, red envelopes or other kinds of gifts?
Will people feel happy when receiving an expensive gift?

Is it hard to choose a gift?
When do people normally send gifts to others?
5  P2  公共场所丢物品
Describe an occasion that you lost something in public
You should say:
What you lost
When and where you lost it
What you did to find it
And explain how you felt about it
P3
What do people often feel after losing things?
What can we do to reduce the possibility of losing things?
What kinds of people may lose things often?
Is it effective to offer rewards to find lost things?
What will people do when losing things?
What kinds of things do people usually lose?
6  P2  节约时间的方法/改变
Describe a way/change that helps you save a lot of time
You should say:
What it is
How you implement it
How difficult it is
And explain how you feel about the way/change
P3
What can people do to save time?
Does technology help people save time? How and why?
Do you think parents should be responsible for teaching children to save time?
Do people who can manage time well become successful more easily?
Is it necessary for children to learn time management?
What can schools do to help students learn time management?
