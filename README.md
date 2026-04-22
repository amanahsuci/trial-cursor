# YouTube Content Strategy for B2B SaaS — Research Project

## Topic

How B2B SaaS companies build and execute YouTube content strategies that generate pipeline and brand awareness.

## Why This Topic?

YouTube is one of the most underrated long-term content distribution platforms in B2B. Unlike social posts that disappear in 48 hours, YouTube videos compound over time — functioning simultaneously as an SEO asset, a sales enablement tool, and a thought leadership channel.

B2B SaaS companies that commit to YouTube early build durable inbound pipelines that paid channels can't replicate. This research project maps how the best practitioners actually do it.

## Why These Experts?

Ten practitioners were selected based on the following criteria:

- **Active creators** — they publish their own content, not just advise others
- **Proven, tangible results** — their YouTube or content strategy has produced measurable business outcomes (pipeline, ARR, community growth)
- **B2B specificity** — their focus is on B2B SaaS, not general creator or consumer content

The goal was to avoid the first page of Google results and find people whose content reflects real operational experience — practitioners who have built channels, grown audiences, and tied content to revenue.

## Selected Experts

| # | Expert | Role | LinkedIn |
|---|---|---|---|
| 1 | Sam Oh | VP of Marketing @ Ahrefs | linkedin.com/in/sam-oh-845930142 |
| 2 | Tim Soulo | CMO & Product Advisor @ Ahrefs | linkedin.com/in/timsoulo |
| 3 | Dave Gerhardt | Founder @ Exit Five | linkedin.com/in/davegerhardt |
| 4 | Ross Simmonds | Founder & CEO @ Foundation Marketing | linkedin.com/in/rosssimmonds |
| 5 | Lenny Rachitsky | Author of Lenny's Newsletter & Podcast | linkedin.com/in/lennyrachitsky |
| 6 | Peep Laja | Founder @ Wynter | linkedin.com/in/peeplaja |
| 7 | Rand Fishkin | Co-founder @ SparkToro & Alertmouse | linkedin.com/in/randfishkin |
| 8 | Wes Bush | Founder @ ProductLed | linkedin.com/in/wesbush |
| 9 | Dan Martell | Founder @ SaaS Academy | linkedin.com/in/danmartell |
| 10 | Kyle Poyar | Author of Growth Unhinged | linkedin.com/in/kyle-poyar |

Full annotations and selection rationale for each expert: [`/research/sources.md`](./research/sources.md)

## Repository Structure

```
/research
  sources.md                        # All experts with links, annotations, and rationale
  /linkedin-posts
    sam_oh_linkedin_posts.md
    tim_soulo_linkedin_posts.md
    dave_gerhardt_linkedin_posts.md
    ross_simmonds_linkedin_posts.md
    lenny_rachitsky_linkedin_posts.md
    peep_laja_linkedin_posts.md
    rand_fishkin_linkedin_posts.md
    wes_bush_linkedin_posts.md
    dan_martell_linkedin_posts.md
    kyle_poyar_linkedin_posts.md
  /youtube-transcripts
    [transcripts organized by author and video]
  /other
    [supplementary materials]
```

## What Was Collected

**LinkedIn Posts** — manually collected from each expert's public profile (April 2026). Posts were selected for recency and topical relevance to B2B content and YouTube strategy. Video-only posts without caption text were excluded.

**YouTube Transcripts** — collected via Supadata API. Transcripts are organized by author and include video title, URL, publish date, and full transcript text.

## Collection Method

- LinkedIn posts: manually collected and formatted as structured Markdown files
- YouTube transcripts: retrieved via Supadata transcript API, parsed and organized by video
- Date range: April 2026
- All sources are publicly available content

## Status

- [x] Expert list finalized
- [x] LinkedIn posts collected and formatted
- [x] YouTube transcripts collected and formatted
- [x] `sources.md` completed with full annotations