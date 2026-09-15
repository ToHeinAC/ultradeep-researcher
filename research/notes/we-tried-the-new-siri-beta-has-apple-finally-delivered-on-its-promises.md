---
title: We Tried The New Siri Beta - Has Apple Finally Delivered On Its Promises?
id: we-tried-the-new-siri-beta-has-apple-finally-delivered-on-its-promises
tags:
- apple-earnings-durability-thesis-b8b3f1
- locus-ai-late-follower-chosen-vs-revealed
created: '2026-09-13T11:30:10.196551Z'
updated: '2026-09-15T19:32:22.183957Z'
source: https://www.slashgear.com/2204931/new-siri-apple-intelligence-ios-27-test-review-what-works-or-doesnt/
source_domain: www.slashgear.com
fetched_at: '2026-09-13T11:30:10.172331Z'
fetch_provider: crawl4ai
status: review
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'SlashGear hands-on review (iOS 27 developer beta, pre-final-release) of
  the long-delayed ''personal context'' Siri first promised at WWDC 2024, tested on
  iPhone/iPad. Verdict: the new Siri (built on Google Gemini) is ''effectively on
  par with the original 2024 demo'' -- surfacing personal data across Messages, Photos,
  Notes, purchase and reading history via natural queries, with strong on-screen awareness.
  Substantive rollout friction: (1) personal-context indexing took over a week on
  iPad and days on iPhone with ~200GB of data; (2) despite ''on-device first'' positioning,
  complex requests route through Private Cloud Compute and stall without good connectivity;
  (3) usefulness scales with depth in Apple''s own apps versus third-party apps like
  Gmail/WhatsApp. States Apple paid $250 million to settle claims from buyers who
  purchased iPhones expecting the 2024-promised Siri, delayed roughly two years. (Summary
  corrected: an earlier auto-summary wrongly said 50 million; the article body says
  $250 million.)'
---

# We Tried The New Siri Beta - Has Apple Finally Delivered On Its Promises?
By [Jordan Wirth](https://www.slashgear.com/author/jordanwirth/) June 30, 2026 4:30 pm EST
Cheng Xin/Getty Images
Add SlashGear on Google:
Preferred Source [Google Discover](https://profile.google.com/@slashgear)
Two years. Count 'em, it's been two years since [Apple Intelligence was unveiled in 2024](https://www.slashgear.com/1642396/apple-intelligence-best-features-iphone/) for iOS 18. The showstopper feature Apple presented at the time was a much-needed Siri upgrade boasting chatbot smarts paired with deep personal contextual awareness. That Siri was delayed. Repeatedly. Things got so bad that Apple coughed up $250 million to disgruntled users who bought iPhones for the new Siri, and rumors swirled that the entire demo had been a Silicon Valley fever dream. At long, long last, though, we have 2024's Siri via the OS 27 Developer Beta. Is it the princess that was promised?
I've been running the [iOS and iPadOS 27 Developer Beta](https://www.slashgear.com/2190962/how-to-download-ios-27-beta-iphone/) since it first released, and ever since I got off the Siri waitlist and both devices finished indexing, I've been throwing everything I could think of at Siri. Complex, unusual questions reminiscent of WWDC 2024's demo (and WWDC 2026's demo) to see whether Apple finally stuck the landing.
Please bear in mind this is all based on early OS 27 beta software, not the final product, so there were plenty of non sequitur answers, misunderstandings, and bugs. I am writing this with the assumption that by the time the full public release happens in September, Apple will have fixed most or all of the issues that I experienced. Here's how it went.
## Two years late, but worth the wait
Jordan Wirth/SlashGear
I won't leave you in further suspense: Yes, this new Siri is effectively on par with the original 2024 demo. Gone are the days of it completely misunderstanding basic requests, or hitting you with a "here's what I found on Google." It's a back-and-forth chatbot experience no different from Gemini or Claude, providing sources you can verify. Personal context is what sets it apart from the competition. WWDC 2024 showed a Siri that knows you intimately via your iCloud account content, and can surface emails, conversations, notes, photos, and more to serve as a helpful digital assistant.
Let me give some examples. I asked it what my Japanese homework was and it translated the conversation with my tutor to figure it out; it guessed when I had purchased a specific model of keyboard by recognizing it in my photos; it told me when and for how much I had sold a device online; when asked whether or not I had been to the place that inspired the "Spirited Away" movie, it pulled up my pictures from my Taiwan trip; it told me which book in the "Saxon Stories" series came next, knowing the ones I had read so far; when asked about my article on [switching to Mac from Windows](https://www.slashgear.com/1630218/switching-from-windows-to-mac-is-it-worth-it/), it summed up my conclusion. I could give examples all day, but the point is, the new Siri works as advertised.
To be abundantly clear, there were plenty of misfires. But when it works (and it does more than it doesn't), it works exceptionally well. I rarely had to baby it; I asked the questions above as vaguely as possible, and Siri often figured out from my personal context what I meant without follow-up clarification. For early beta software, this is incredibly promising.
## Indexing may take an eternity
Jordan Wirth/SlashGear
In order to understand your personal context enough to help you, Siri requires indexing. You'll see this when you open the Settings app on your device. Indexing is essential to get useful answers, so if you use Siri before the indexing is complete, your experience will be subpar. The problem is indexing — at least during the beta — can take an annoyingly long time to complete.
Since I was running the beta on both iOS and iPadOS, I tried two different approaches. On the iPad, I just used it normally; I charged the device when it was low and then just left it there when not in use. As a result, indexing took _forever._ Literally over a week. On my iPhone, I left it plugged in for hours at a time, and it finished in a couple of days. It's likely Apple will figure out how to make indexing go faster when OS 27 officially releases, but I can't imagine it'll take less than a couple of days for most people unless you leave your phone plugged in all night.
I should mention here that I don't have a huge amount of content on my devices and in iCloud, either. Maybe 200GB total for photos, iCloud Drive, notes, etc. So if someone has a much larger pool of personal content, I worry the indexing will keep them waiting for even longer before they can really use Siri. Here's to hoping it's not like that [common problem on iOS 26](https://www.slashgear.com/2054227/ios-26-common-problems-fixes/) where the reindexing after every update makes your phone get hot and zaps its battery — except this time, it temporarily kneecaps Siri for a few days.
## Siri may be on-device first, but you'll still need internet
Jordan Wirth/SlashGear
When I finally got off the Siri waitlist, I just happened to be away from home in a place with terrible Wi-Fi and cell signal. "Not a problem," I thought. "The new Siri is all on-device, so I should be able to use it comfortably with local data." Boy, was I wrong. Simple requests like setting reminders worked. Anything more complex than that — even if Siri had the info right there in front of its face — failed. This is because, I learned, even though the processing _does_ happen on device, Siri relies on Apple's Private Cloud Compute servers to know how to approach a request. My complex requests either took forever or failed until I found [a good Wi-Fi network](https://www.slashgear.com/1910787/things-in-home-negatively-affecting-disrupting-wifi-connection/).
In my view, Apple would do well to make this abundantly clear upon the official release. People are going to misunderstand the "on-device" part to mean that they could, in theory, go off the grid with their iPhone and have a fully functional digital assistant, which they won't. And of course, nobody's thrilled about these very personal requests being slingshotted into the cloud where they can only hope and pray that their data privacy won't be abused. None of this is helped by the fact that the new Siri is built on Google's Gemini.
Look, I get it. Most of us are connected to Wi-Fi and/or cellular virtually 24/7 with few exceptions. Just be prepared for Siri's new spinning thinking dots to take longer if you're on bad Wi-Fi.
## The deeper you're in the Apple ecosystem, the better (for now)
Runrun2/Shutterstock
The more thoroughly integrated your life is into Apple's services and apps — Photos, iMessage, Calendar, Contacts, Notes, Reminders, Music, Podcasts, etc. — the more useful and effective OS 27's Siri will be for you ... which could also be one of its biggest downsides. People who use, say, the Gmail app for email, WhatsApp for friend and family chats, and Microsoft OneDrive for files may come away disappointed if Siri can't talk to or source data from their preferred non-Apple apps.
I experienced this myself to an extent during my testing. Most of my chats are not in iMessage, so any questions leveraging previous conversations with family and friends fell on deaf ears. This was frustrating even though I have the lion's share of my personal data in Apple's ecosystem. I can't imagine how much more frustrating this will be for someone who uses even fewer Apple services — or none.
Having said that, this may just be an early beta limitation. Apps that incorporate App Intents and MCP (frameworks that basically make it easier for Siri to request data from third-party apps) could potentially make it irrelevant which apps you use. After the OS 26 release, it took time for apps to adopt Apple's Liquid Glass design language, but eventually most of them did. Give OS 27 a year or so to mature and I'd bet all the major apps will have already jumped on the App Intents bandwagon, making Siri capable for all users.
## On-screen awareness is the killer feature
Jordan Wirth/SlashGear
Everything I've mentioned so far is cool, but what's going to really be a game changer is on-screen awareness. At any time, in any app, you can summon Siri and ask it questions about what you see on screen, and have Siri act on your behalf. During the original WWDC 2024, the demo showed the presenter's Siri grabbing a driver's license number from a picture and inserting it into a form seamlessly with one request. You can do that now with this Siri, and so much more.
For example, I asked Siri to send the note I was viewing as a PDF to an email address; I asked it to screenshot the current page I was looking at and send it to one of my contacts; with Safari open, I asked it to open a new tab and show me the iPad Pro product page; in Google News, I asked it to identify the person in one of the headline images, and it did so; I asked it to "set a reminder for this" when on the PlayStation page for "Grand Theft Auto 6," and it did so; while looking at a picture of a receipt, it was able to copy all the text to a note. And a lot more.
I know these are random examples that may not necessarily be useful, but they demonstrate an incredible amount of potential beyond Apple's iffy recommendations during WWDC 2026 to make themed recipes for parties. As long as there's clear information on the screen, Siri can seemingly perform any basic action on it, and that's going to save you a lot of time with tedious tasks that you might have otherwise done manually.
## Recommended
