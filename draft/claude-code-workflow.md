# Claude Code Workflow

## 工作流

Anthropic 在 2025 年 7 月 24 日發布文章 [AnthropicAI How Anthropic teams use Claude Code](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code) 介紹了 Anthropic 各部門如何利用 **Claude Code** 來加速工作流程、自動化繁瑣任務、處理複雜專案，以及協助非技術角色也能構建更多專案或解決方案。

以下是 Claude 整理的表格：
| 團隊 | 主要使用案例 | 團隊影響/效果 |
|------|-------------|---------------|
| **資料基礎設施** | • Kubernetes 除錯診斷<br>• 為財務團隊建立純文字工作流程<br>• 新員工程式庫導覽<br>• 會話結束文件更新<br>• 多實例並行任務管理 | • 無需專業知識解決基礎設施問題<br>• 加速新人培訓<br>• 增強支援工作流程<br>• 實現跨團隊自助服務 |
| **產品開發** | • 自動接受模式快速原型開發<br>• 核心功能同步編程<br>• 測試生成和錯誤修復<br>• 程式庫探索 | • 更快的功能實作<br>• 提升開發速度<br>• 透過自動測試提升程式碼品質<br>• 更好的程式庫探索 |
| **資安工程** | • 複雜基礎設施除錯<br>• 程式碼審查和分析<br>• 文件整合和操作手冊<br>• 測試驅動開發工作流程<br>• 情境切換和專案導入 | • 減少事件解決時間（10-15 分鐘 →5 分鐘）<br>• 改善安全審查週期<br>• 增強跨功能貢獻<br>• 更好的文件工作流程 |
| **推理系統** | • 程式庫理解和新人培訓<br>• 單元測試生成與邊界案例涵蓋<br>• 機器學習概念解釋<br>• 跨語言程式碼翻譯<br>• 指令回憶和 Kubernetes 管理 | • 加速 ML 概念學習（減少 80%研究時間）<br>• 更快的程式庫導覽<br>• 全面的測試覆蓋<br>• 消除語言障礙 |
| **資料科學與 ML 工程** | • 建立 JavaScript/TypeScript 儀表板應用<br>• 處理重複性重構任務<br>• 建立持久性分析工具<br>• 零依賴性任務委派 | • 實現 2-4 倍時間節省<br>• 在不熟悉語言中建立複雜應用<br>• 從一次性轉向持久性工具<br>• 直接改善模型洞察 |
| **產品工程** | • 第一步工作流程規劃<br>• 跨程式庫獨立除錯<br>• 透過實際使用進行模型迭代測試<br>• 消除情境切換開銷 | • 增加處理不熟悉領域的信心<br>• 顯著節省情境收集時間<br>• 更快的輪調導入<br>• 提升開發者滿意度 |
| **成長行銷** | • Google Ads 創意自動生成<br>• Figma 外掛大量創意製作<br>• Meta Ads MCP 伺服器用於廣告活動分析<br>• 使用記憶系統的進階提示工程 | • 重複性任務大幅節省時間<br>• 創意輸出增加 10 倍<br>• 像更大的團隊一樣運作<br>• 戰略焦點轉移 |
| **產品設計** | • 前端優化和狀態管理變更<br>• GitHub Actions 自動票務<br>• 快速互動式原型製作<br>• 邊緣案例發現和系統架構理解<br>• 複雜文案變更和法律合規 | • 轉變核心工作流程<br>• 執行速度提升 2-3 倍<br>• 週級到小時級的週期時間<br>• 兩種不同的用戶體驗 |
| **RL 工程** | • 有監督自主的功能開發<br>• 測試生成和程式碼審查<br>• 除錯和錯誤調查<br>• 程式庫理解和呼叫堆疊分析<br>• Kubernetes 操作指導 | • 實現實驗性方法<br>• 加速文件製作<br>• 有限制的加速（首次成功率約 1/3） |
| **法務** | • 為家庭成員的自訂無障礙解決方案<br>• 法務部門工作流程自動化<br>• 團隊協調工具<br>• 解決方案驗證的快速原型製作 | • 在 Claude.ai 中規劃，在 Claude Code 中建立視覺優先方法<br>• 原型驅動創新 |

**一般工作流**

適用多類型問題的一般工作流

1. **探索**：
   - 讓 Claude Code 閱讀相關檔案、圖片或 URL。
   - **提示**：此階段不要讓 Claude Code 寫程式碼。
   - 可利用 **子代理** 幫助查細節、調查問題，保留更多上下文。
2. **規劃**：
   - 要求 Claude Code 制定解決方案計劃。
   - 使用關鍵字控制思考深度：
     - `think` < `think hard` < `think harder` < `ultrathink`
   - 結果合理時，可讓 ClaudeCode 建立文檔或 GitHub issue 記錄。
3. **編碼**：
   - 請 Claude Code 實現程式碼，並在過程中檢查合理性。
4. **提交**：
   - 提交 PR，並可更新 README、changelog。

**_第 1-2 步至關重要，否則 Claude 可能直接跳到寫代碼。_**

**快速使用流**

適用於快速修復 lint、生成樣板程式碼

- 指令：`claude --dangerously-skip-permissions`

可能造成資料丟失 / 系統損壞 / 資料洩露（提示注入攻擊）。**建議**在**無網路容器**中使用，例如 Docker。

**測試驅動開發（TDD）**

適用於單元 / 集成 / 端到端測試可驗證的功能

1. **寫測試**：
   - 要求 Claude Code 根據預期輸入/輸出編寫測試。
   - 強調「不要寫功能程式碼」。
2. **驗證測試失敗**：
   - 明確要求先執行測試，確認失敗。
3. **提交測試**。
4. **編寫與迭代**：
   - 要求 Claude 編寫實現程式碼，且「不要修改測試」。
   - 多輪迭代直到測試通過。
   - 也可用子代理檢查是否**過擬合測試**。
5. **最後提交最終程式碼**。

**UI 工作流**

適用於設計 / UI 驗證

1. 提供 Claude Code 圖片或 UI 設計圖。
2. Claude Code 根據設計實現程式碼，輸出結果並截圖。
3. 對比 → 修改 → 截圖 → 再迭代。
4. 滿意後提交。

**Git、GitHub 操作**

可處理多數 git 操作：

- **查歷史**：版本差異、作者、設計原因。
- **提交訊息**：自動生成，包含完整上下文。
- **複雜操作**：回滾、rebase 衝突解決、補丁移植。

還可代理 GitHub 交互：

- 建立 PR（支援「pr」簡寫）。
- 一鍵修正 PR 上的簡單 review 意見。
- 修復 build 錯誤或 linter 警告。
- 批次處理 open issues（分類、整理）。

**Jupyter Notebook**

適用於資料科學、研究

- 讀寫 `.ipynb` 文件，並解釋輸出（含圖表）。
- 在 VS Code 與 Notebook 並排使用效果最佳。
- 可要求**美化 notebook** 或 **優化資料視覺化**。

**Spec 驅動開發（Spec-driven development）**

這是一個近期蠻被看好的 AI coding 開發工作流。以 **Amazon** 的 **Kiro IDE** 為例，Spec 驅動開發的流程大致分為三步：

1. **Requirements（需求規格）**

   - 用自然語言寫清楚「功能要達到什麼」、「使用者情境」、「成功驗收標準」。
   - 例如：

     > 使用者輸入 email，系統必須驗證格式，若錯誤需提示訊息。

2. **Design（設計規格）**
   - 定義系統架構、資料流、API 介面、數據結構。
   - 例如：
     - UI 元件：Email 輸入框
     - 驗證函式：`validate_email(email: str) -> bool`
     - 錯誤提示元件：ErrorBanner
3. **Tasks（實作任務）**
   - 把設計切分成小的可交付任務。
   - 例如：
     - Task 1: 建立 `validate_email` 函式
     - Task 2: 建立 UI 元件 EmailInput
     - Task 3: 整合驗證與錯誤提示

在每一步，規格文件都是**可審核的、可重用的、可持續更新的**。

其價值在於

- **可追蹤性（Traceability）**
  - 每行程式碼都能追溯回需求。
- **協作性（Collaboration）**
  - 團隊成員可先討論 Spec，而不是直接討論 AI 生成的程式碼。
- **品質（Quality）**
  - 減少 AI 產生的隱性錯誤。
  - 可以與靜態檢查、測試覆蓋率整合。
- **一致性（Consistency）**
  - 多代理（multi-agent）開發可共用 Spec，降低上下文遺失問題。

關於這個工作流可以參考（借鑑 Kiro 的 Spec 驅動開發工作流實現的 Claude Code 工作流方法） [gotalab/cc-sdd](https://github.com/gotalab/claude-code-spec)

**Vibe Coding**

由 **Andrej Karpathy** 在 **2025 年 2 月**於他的推文中首次提出 Vibe Coding，[：「There's a new kind of coding I call ‘vibe coding’, where you fully give in to the vibes, embrace exponentials, and forget that the code even exists」](https://x.com/karpathy/status/1886192184808149383)

![andrej-karpathy-x-vibe-coding](../assets/img/claude-code-workflow/andrej-karpathy-x-vibe-coding.png)

是一種 AI 輔助的編程方式，開發者用自然語言描述需求，由大型語言模型（LLM）生成程式碼，不需審閱原始碼，只透過執行結果和互動來驗證與改進，重心從「寫程式」轉為「引導 AI、測試和反饋」。同時也被視為低程式碼（low-code）與無程式碼（no-code）技術上的演進。從 2010 年代的 4GL、模型驅動開發，到 2021 年的 AI 編程助手（例如 GitHub Copilot），再加上 2022 年 ChatGPT 的出現，到了 2025 年形成一個新興主流趨勢。

隨後有以下幾個現象

- 多家媒體與專家重視這一概念，例如 **Ars Technica**、**The Observer**、**Times of India** 都於 2025 年早期報導，探討其潛力與風險。
- **Y Combinator** 表示，2025 冬季批次中有 **25% 的新創公司**幾乎完全依賴 AI 生成程式碼（codebase nearly 95% AI-generated）。
- **Garry Tan（Y Combinator CEO）** 認為 vibe coding 可能讓小團隊完成過往需 50–100 人才能做的工作量，顯著提高效率。
- **Tom's Guide** 與 **Financial Times** 等也指出，這種方式為非程式開發者提供了創造工具的可能性，但也引發專業程式設計師對程式品質與安全性的疑慮。

除此之外，值得注意的是，不僅只有 Vibe Coding，近期就連 Hacker 也開始 Vibe Hacking！？

由 iThome 報導 [iThome - 不只 Vibe Coding，駭客正把 Claude Code 用於 Vibe Hacking](https://www.ithome.com.tw/news/170951)，有人將 Claude Code 作為 AI 代理整合至攻擊鏈，不再只是建議，而是實際執行整個攻擊流程。其**受害範圍**至少影響 17 個組織，涵蓋政府、醫療、緊急應變、宗教等領域，勒索金額超過 50 萬美元。

主要有以下幾個操作

- 在 Kali Linux 上使用 Claude Code 作為統合平台，從 OSINT 探查、VPN 掃描、憑證竊取到網路滲透與橫向移動，Claude Code 決定入侵策略、選擇洩露資料類型、撰寫具心理操控效果的勒索話術，並規劃財務評估與勒索手段。
- 使用 `CLAUDE.md` 設定 TTP（Tactics, Techniques, Procedures），Claude Code 可依此批次化操作數千 VPN 端點，並開發混淆隧道與自製 TCP 代理，加入字符串加密、反除錯與檔名偽裝（如偽裝為 MSBuild.exe、devenv.exe、cl.exe）。
- Claude Code 甚至分析受害者的財務狀況，以估算可承受的勒索金額，並自動生成強烈視覺警示的 HTML 勒索頁面，嵌入開機流程，使受害者無法逃避。

其他濫用案例：

1. 北韓透過 Claude Code 偽造專業履歷與形象，甚至在面試與工作中自動產出程式碼與英文溝通內容，進入美國大型科技公司，違反國際制裁；Anthropic 已封鎖帳號並通報主管機關。
2. 一名英國駭客（編號 GTG-5004）利用 Claude Code 開發、銷售具加密、反分析功能的勒索軟體，每套售價約 400–1,200 美元。若無 AI 幫助，開發者根本無法完成這類惡意軟體的實作。

相關調查報告可以看 Anthropic 發表的這篇文章 [AnthropicAI Detecting and countering misuse of AI: August 2025](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025)

## 提示詞工程（Prompt Engineering）

與 Claude Code 互動，勢必要更好的讓它知道該做的是甚麼，因此 Prompt 的設計相當重要。

關於 Prompt 的設計可以參考 [Anthropic Prompt engineering overview - Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)，或是 **Code w/ Claude** 演講的分享 [Anthropic Prompting 101 | Code w/ Claude](https://youtu.be/ysPbXH0LpIE?si=FHE0TTKb6zSxDNr9)。

**Prompt Structure**

1. **角色定位與任務描述（1–2 句）**

   明確設定 AI 的身份與目標，用簡短語句交代核心任務。

2. **動態與檢索資訊**

   提供即時或個人化的資料（例如使用者偏好、地點、上下文），作為回應的依據。

3. **詳細任務指令**

   清楚列出執行步驟與規則，確保 AI 按指定流程處理。

4. **範例 / n-shot（選填）**

   以示例引導模型，展示輸入與輸出的對應方式。

5. **關鍵指令重申**

   在長提示的結尾再次強調最重要的規則，避免模型偏離。

![prompt-structure](../assets/img/claude-code-workflow/prompt-structure.png)

若要處理更複雜的任務時，也可以參考以下結構，擴展更多上下文，使得它可以更好理解上下文資訊

- **任務脈絡（Task Context）**

  用 1–3 句交代角色、目標、受眾與成功定義。

  例如：「你是 ⋯；目標是 ⋯；成功 = ⋯。」

- **語氣設定（Tone & Style）**

  明確指定語氣、風格、嚴謹度與讀者假設。

  例如：「專業但親切；避免行話；面向新手 PM。」

- **參考資料（Background Docs & Media）**

  列出可用的靜態素材與其用途/優先序；標示缺漏時的退場策略。

  例如：「主參考 A，次參考 B；若缺 A，依 B→C 順序補。」

- **作業規則（Instructions & Constraints）**

  以「必須／不得／可以」三層條款描述步驟、判準、邊界與超時/錯誤處理。

  例如：「必須：對齊產品定義；不得：暴露內部推理。」

- **範例（Examples / N-shot）**

  提供 1–3 組高品質對照範例；標註為「示意，非抄寫」。

  例如：範例覆蓋常見變體與邊界情形。

- **對話歷史（Conversation History）**

  只保留與本輪決策必需的片段，並以要點化摘要注入。

  例如：「先前已確定：KPI=CTR；時區=Asia/Taipei。」

- **本輪請求（Current Turn Request）**

  用可驗收的單句工作說明 + 交付時限/範圍。

  例如：「請在 600 字內產出方案比較表與建議。」

- **思考引導（Reasoning Hints）**

  引導「先思後寫」，但**避免要求輸出長推理**。

  例如：「先列關鍵假設再給結論；僅輸出結論與依據摘要。」

- **輸出格式（Output Formatting / Schema）**

  指定結構、欄位、順序與單位；必要時給 JSON schema 或 Markdown 骨架。

  例如：「輸出：# 概覽 → 表格 → 建議 → 風險。」

- **預填回應（Assistant Prefill）**

  （供支援的供應商使用）預置回應開頭以定調或鎖定格式。

![prompt-structure-plus](../assets/img/claude-code-workflow/prompt-structure-plus.png)

Claude Code 本身的 System Prompt 可以參考 [ vivek What makes Claude Code so damn good (and how to recreate tha…](https://minusx.ai/blog/decoding-claude-code/#appendi) 中 Appendix 的部分。這篇文章是在**解構 Claude Code 為什麼好用**，並整理出可以借鏡的 AI 系統設計原則。

## 多子代理協作

[Anthropic sub-agents - Anthropic](https://docs.anthropic.com/zh-TW/docs/claude-code/sub-agents)

可以使用多個 agent 協作，例如：

一個 Claude Code 寫程式碼，另一個審查或測試。類似多工程師協作，分開上下文有時更好：

- **流程**：
  1. agent A：負責寫代碼。
  2. agent B：清空上下文（`/clear`）或在另一終端啟動，負責審查或測試代碼。
  3. agent C：重新讀取代碼與審查意見，根據反饋修改代碼。
- 其他：
  - agent A 負責寫測試，Claude B 負責寫通過測試的代碼。
  - agent 實例之間可透過「草稿本」協作（指定誰寫、誰讀）。
- **優勢**：分工清晰，避免單一上下文過載，效果優於單 Claude 全包。

**分工開發**

多模塊開發或分工並行

- **做法**：
  1. 建立 3–4 個 git clone，分別放在不同資料夾。
  2. 在不同終端標籤頁打開每個資料夾。
  3. 在各資料夾啟動一個 Claude，分配不同任務。
  4. 輪流檢查進度、批準/拒絕權限請求。

如此一來，就可以讓每個 agent 專注於一個子任務，並行推進使用。

**git worktree**

在同一專案內同時處理多分支任務

- `git worktree` 可將同一 repo 的多個分支檢出到不同資料夾。
- **流程**：

  ```bash
  git worktree add ../project-feature-a feature-a
  cd ../project-feature-a && claude
  ```

  - 按需建立多個 worktree，分別在不同終端或 IDE 啟動 Claude Code。

- **建議**：

  - 命名規範統一（如 `feature-a`、`feature-b`）。
  - 每個 worktree 一個終端 tab。
  - Mac 可用 iTerm2 提示 Claude 請求。
  - IDE 視窗區分不同 worktree。
  - 完成後清理：

    ```bash
    git worktree remove ../project-feature-a
    ```

Claude Code 可同時在專案不同部分工作，避免等待或衝突。

**無頭模式 + 自訂腳本**

**適用情境**：大規模自動化 / 整合到流水線

- **指令**：`claude -p` 方式使用 Claude Code。
- **兩種用法**：

  1. **批量處理**：

     - 讓 Claude Code 先寫腳本產生任務清單（如需遷移的檔案列表）。
     - 程式化迴圈呼叫 Claude Code：

       ```bash
       claude -p "migrate foo.py from React to Vue. When you are done, return OK or FAIL." \
         --allowedTools Edit Bash(git commit:*)
       ```

     - 多次運行，調整提示直到滿意。

  2. **pipline 整合**：

     - 將 Claude Code 接到處理管線：

       ```bash
       claude -p "<prompt>" --json | your_command
       ```

     - 透過 JSON 輸出方便自動化。

## 工具

以下是一些實用的 Claude Code 相關工具與資源

### 資源集

- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Claude Code 相關資源大全
- [claude-code-templates](https://github.com/davila7/claude-code-templates) - Claude Code 模板集

### 一般工

- [ccundo](https://github.com/RonitSachdev/ccundo) - Claude Code 撤銷操作工具
- [ccusage](https://github.com/ryoppippi/ccusage) - Claude Code 使用情況統計
- [happy](https://github.com/slopus/happy) / [Claude-Code-Remote](https://github.com/JessyTsui/Claude-Code-Remote) - 遠端協作工具
- [claude-code-router](https://github.com/musistudio/claude-code-router) - Claude Code 路由管

### 工作流與多代理協

- [claude-code-settings](https://github.com/feiskyer/claude-code-settings) - Claude Code 設定配置
- [agents](https://github.com/contains-studio/agents) - 代理協作框架
- [SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) - SuperClaude 框架
- [claude-task-master](https://github.com/eyaltoledano/claude-task-master) - 任務管理工具
- [claude-flow](https://github.com/ruvnet/claude-flow) - 工作流管理
- [claude-squad](https://github.com/smtg-ai/claude-squad) - 多代理協作平台
- [claude-code-spec-workflow](https://github.com/Pimzino/claude-code-spec-workflow) - Spec 驅動開發工作

### 交互界面與 IDE 集

- [gooey](https://github.com/getAsterisk/gooey) - GUI 界面工具
- [claudecode.nvim](https://github.com/coder/claudecode.nvim) - Neovim 整合外掛

## Claude Code in Action

除此之外，Claude Code 還可以幫助開發者整合 Github Action 工作流，只需在任何 PR 或 issue 中簡單地提及 **`@claude`**，Claude 就能：

- **自動分析程式碼**：審查差異、檢查潛在問題並提出優化建議。
- **建立與更新 PR**：根據需求自動生成新的 Pull Request，或更新既有的修改。
- **實作新功能**：將自然語言需求轉化為實際程式碼，直接推送到分支。
- **修復錯誤與漏洞**：快速定位問題並提交修正程式碼。

使得開發團隊能在 GitHub 中，使用 Claude Code 支援，大幅提升協作與開發效率。

[skilljar Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)
