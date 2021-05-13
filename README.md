
# Wikihow Video Generator

Generator markdown and video from Wikihow pages.


## Dependencies

Python 3.9

MongoDB

node



## Features

[x] Fetch wikihow pages and save to MongoDB

[x] Render wikihow pages to markdown

[X] Convert markdown to slides(By marp-cli)

[ ] Create videos from slides

  
## Usage

### Fetch Wikihow pages

```bash
python main.py https://zh.wikihow.com/%E6%89%93%E8%B4%A5%E5%91%A8%E4%B8%80%E6%97%A9%E6%99%A8%E5%BF%A7%E9%83%81%E7%97%87
```

### Render Wikihow pages to Markdown

```bash
 python .\main.py render "如何制作免洗洗手液: 8 步骤" --out out.md
```

### Convert Markdown to Slides

```bash
npx @marp-team/marp-cli --pptx out.md
```
## Authors

- [@duyixian1234](https://www.github.com/duyixian1234)

  