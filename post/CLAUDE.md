# Claude Code 博客文章寫作指南

## 文章結構規範

### HTML 模板結構
每篇文章應包含以下基本結構：

```html
<!DOCTYPE html>
<html lang="zh-TW"> <!-- 中文文章使用 zh-TW -->
<head>
    <!-- Meta 資訊 -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <meta name="XD3an" content="All-In-One" />
    <meta name="description" content="具體且吸引人的描述，包含關鍵字" />
    <meta name="author" content="XD3an" />
    <meta name="keywords" content="相關關鍵字，用逗號分隔" />
    
    <!-- 標題 - 要有吸引力和 SEO 友好 -->
    <title>吸引人且有網路梗的標題</title>
    
    <!-- 基本資源 -->
    <link rel="icon" type="image/x-icon" href="../assets/deer_icon.png" />
    <script src="https://use.fontawesome.com/releases/v6.1.0/js/all.js" crossorigin="anonymous"></script>
    <link href="../css/styles.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="../js/scripts.js"></script>
    
    <!-- 程式碼高亮 (如需要) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    
    <!-- SEO 和社交媒體標籤 -->
    <meta property="og:title" content="標題 | XD3an Blog" />
    <meta property="og:description" content="描述" />
    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://XD3an.github.io/post/filename.html" />
    
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:title" content="標題 | XD3an Blog" />
    <meta name="twitter:description" content="描述" />
    
    <!-- JSON-LD 結構化資料 -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "文章標題",
        "description": "文章描述",
        "author": {
            "@type": "Person",
            "name": "XD3an"
        },
        "datePublished": "YYYY-MM-DD"
    }
    </script>
</head>

<body>
    <!-- Magic Canvas -->
    <canvas id="magic-canvas"></canvas>
    <script src="/js/magic.js"></script>
    
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light" id="mainNav">
        <!-- 標準導航結構 -->
    </nav>
    
    <!-- Header with Background -->
    <header class="masthead" style="background-image: url('../assets/img/文章名稱/background.jpg')">
        <div class="container position-relative px-4 px-lg-5">
            <div class="row gx-4 gx-lg-5 justify-content-center">
                <div class="col-md-10 col-lg-8 col-xl-7">
                    <div class="post-heading">
                        <h1>文章主標題</h1>
                        <h4 class="subheading">副標題</h4>
                        <span class="meta">By XD3an</span>
                    </div>
                </div>
            </div>
        </div>
    </header>
    
    <!-- Main Content -->
    <article class="mb-4">
        <div class="container px-4 px-lg-5">
            <div class="row gx-4 gx-lg-5 justify-content-center">
                <div class="col-md-10 col-lg-8 col-xl-7">
                    <!-- 文章內容 -->
                </div>
            </div>
        </div>
    </article>
    
    <!-- Footer -->
    <footer class="border-top">
        <!-- 標準 footer 結構 -->
    </footer>
</body>
</html>
```

## 標題寫作規則

### 主標題特色
- **有網路梗感**：使用當下流行的網路用語（如「贏麻了」、「破防了」、「yyds」等）
- **吸引眼球**：要讓人忍不住想點進來看
- **面向大眾**：避免「我」的個人視角，使用更通用的描述
- **SEO 友好**：包含相關技術關鍵字

### 標題範例模式
- 「XXX 贏麻了：[效果描述]」
- 「XXX 破防了：[驚人效果]」  
- 「XXX 太狂了吧：[讓人驚嘆的功能]」
- 「XXX 封神之作：[對比描述]」
- 「XXX 直接起飛：[效率提升描述]」

### 副標題規則
- 呼應主標題的風格
- 提供更具體的內容描述
- 保持簡潔有力

## 內容結構規範

### 段落標題層級
- `<h2>` - 主要章節標題
- `<h3>` - 次級章節標題  
- `<p><strong>粗體文字</strong>` - 重點段落標題（不使用 h4）

### 圖片規範
```html
<div style="text-align: center;">
    <img 
        src="../assets/img/文章目錄名稱/圖片名稱.png" 
        alt="圖片描述" 
        class="img-fluid mb-3" 
    />
    <span class="caption text-muted">圖片來源說明</span>
</div>
```

### 程式碼區塊
```html
<pre><code class="language-具體語言">
程式碼內容
</code></pre>
```

### 列表規範
- 使用 HTML `<ul>` 和 `<li>` 標籤
- 保持縮排一致
- 重要項目使用 `<strong>` 加粗

## 資產管理

### 圖片組織
```
assets/img/
└── 文章英文名稱/
    ├── background.jpg        # 文章背景圖
    ├── screenshot-1.png      # 截圖1
    ├── diagram.png           # 圖表
    └── ...
```

### 圖片規範
- 使用相對路徑 `../assets/img/文章名稱/`
- 圖片名稱使用英文和數字，用破折號分隔
- 保持圖片大小適中，優化載入速度
- 統一使用 `img-fluid` class 保持響應式

## 漂浮目錄 (TOC) 規範

如果文章較長，建議加入漂浮目錄：

```html
<!-- CSS 樣式 -->
<style>
.floating-toc {
    position: fixed;
    top: 20%;
    right: 20px;
    width: 280px;
    max-height: 60vh;
    background: white;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    padding: 16px;
    font-size: 14px;
    z-index: 1000;
    overflow-y: auto;
    opacity: 0.95;
}

.floating-toc a.active {
    background-color: #ff6b35; /* Claude 橘色 */
    color: white;
}
</style>

<!-- HTML 結構 -->
<div class="floating-toc" id="floatingToc">
    <div class="toc-content">
        <ul>
            <li><a href="#section1" class="toc-h2">章節1</a></li>
            <li><a href="#section2" class="toc-h3">子章節</a></li>
        </ul>
    </div>
</div>

<!-- JavaScript 功能 -->
<script>
// 滾動高亮和平滑滾動功能
</script>
```

## 文章發布流程

### 1. 建立文章檔案
- 檔案命名：`文章英文名稱.html`
- 放置位置：`/post/` 目錄

### 2. 準備資產
- 在 `/assets/img/` 下建立同名資料夾
- 上傳所需圖片和資源

### 3. 更新首頁
在 `index.html` 中新增文章條目：

```html
<div class="post-preview">
    <a href="post/文章名稱.html">
        <h2 class="post-title">文章主標題</h2>
        <h6 class="post-subtitle">文章副標題</h6>
    </a>
    <p class="post-meta">
        Posted by
        <a href="#!">XD3an</a>
        on 發布日期
    </p>
</div>
<hr>
```

## 注意事項

### 內容指導原則
- 所有內容必須用於**教育和防禦性安全研究**
- 保持專業性和教育價值
- 避免提供可能被惡意使用的具體攻擊代碼

### SEO 最佳實踐
- 標題包含主要關鍵字
- Meta description 簡潔且吸引人
- 使用適當的標題階層 (H1 > H2 > H3)
- 圖片加上 alt 屬性
- 內部連結到相關文章

### 技術細節
- 所有路徑使用相對路徑
- 確保在不同裝置上的響應式顯示
- 程式碼語法高亮正確配置
- 載入速度優化

## 檔案範例

參考現有文章：
- `claude-code-guide.html` - 完整功能文章範例
- `MD-part1.html` - 基礎文章結構範例

遵循這些規範可以確保文章的品質和一致性！