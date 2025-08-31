# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML website/blog hosted on GitHub Pages (XD3an.github.io) that focuses on cybersecurity and technical education content. The site features articles about malware development techniques, browser automation, and other security research topics written in both Traditional Chinese and English.

## Site Structure

```
/
├── index.html              # Main homepage listing all blog posts
├── contact.html            # Contact page
├── post/                   # Blog post HTML files
│   ├── MD-part1.html      # Malware Development series posts
│   ├── MD-part2.html
│   ├── MD-part3.html
│   ├── MD-part4.html
│   └── WC.html            # Browser Automation post
├── assets/                 # Static assets
│   ├── img/               # Images organized by post/topic
│   └── deer_icon.png      # Site favicon
├── css/
│   └── styles.css         # Bootstrap-based styling
├── js/
│   ├── scripts.js         # Main site JavaScript
│   └── magic.js           # Canvas animation effects
├── lab/                   # Educational code examples and labs
│   └── Malware-Development-from-Scratch/
├── temp/                  # Draft/template files
└── draft/                 # Draft posts (not published)
```

## Technology Stack

- **Frontend**: Pure HTML5, CSS3, JavaScript (ES6)
- **CSS Framework**: Bootstrap 5.1.3
- **Icons**: Font Awesome 6.1.0
- **Hosting**: GitHub Pages
- **Version Control**: Git

## Development Workflow

### Adding New Blog Posts

1. Create HTML file in `/post/` directory following existing naming convention
2. Add post entry to main `index.html` with:
   - Link to new post
   - Title in both Chinese and English
   - Publication date
   - Author metadata
3. Add corresponding images to `/assets/img/[post-name]/`
4. Update navigation if needed

### Asset Management

- Images are organized by topic/post in `/assets/img/`
- Use relative paths for asset references
- Maintain consistent image naming conventions
- Optimize images for web delivery

### Content Guidelines

- Posts focus on educational cybersecurity content
- Include both Chinese and English titles/subtitles
- Use consistent HTML structure across posts
- Include proper meta tags for SEO

## Deployment

Site is automatically deployed via GitHub Pages when changes are pushed to the main branch. No build process required - static files are served directly.

## Commit Message Convention

Based on git history, use format: `[Update] brief description of changes`

Examples:
- `[Update] update .gitignore`
- `[Update] update post/wc`
- `[Add] new malware development part 5`
- `[Fix] broken image links in contact page`

## Important Notes

- This is an educational cybersecurity blog - all content should be for defensive security research and education only
- Maintain the bilingual (Chinese/English) nature of the content
- Keep the clean, professional design aesthetic
- Ensure all external links work and are appropriate
- Test locally before pushing to ensure no broken links or layout issues