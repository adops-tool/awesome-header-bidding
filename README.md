<div align="center">
  
# Awesome Header Bidding 🎯

**A curated, engineering-first index of the open-source header bidding stack — the wrappers, debuggers, identity modules, and specifications that make programmatic auctions legible and measurable.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

</div>

## 📑 Table of Contents

- [Core Open-Source Frameworks](#-core-open-source-frameworks)
- [Browser Extensions and Debugging Tools](#-browser-extensions-and-debugging-tools)
- [User ID and Identity Modules](#-user-id-and-identity-modules)
- [Analytics, Monitoring and Latency Tools](#-analytics-monitoring-and-latency-tools)
- [Wrappers, Boilerplates and Starter Kits](#-wrappers-boilerplates-and-starter-kits)
- [Price Floors, Timeouts and Optimization Guides](#-price-floors-timeouts-and-optimization-guides)
- [Specifications and Standards](#-specifications-and-standards)
- [Communities and Newsletters](#-communities-and-newsletters)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧩 Core Open-Source Frameworks

The engines that actually run the auction — read these before evaluating any vendor on top of them.

- [Prebid.js](https://github.com/prebid/Prebid.js) - The de facto client-side header bidding wrapper: runs parallel auctions across hundreds of bid adapters and writes winning bids into ad server key-values.
- [Prebid Server (Go)](https://github.com/prebid/prebid-server) - High-throughput Go implementation of the Prebid Server auction engine for web, AMP, mobile, video, and CTV requests.
- [Prebid Server (Java)](https://github.com/prebid/prebid-server-java) - Spring-based Prebid Server implementation with a modular hook framework, commonly deployed where Spring and hook-based modules are preferred.
- [Prebid Mobile Android](https://github.com/prebid/prebid-mobile-android) - Android SDK that requests bids from Prebid Server and renders them through GAM, AdMob, AppLovin MAX, or a custom ad server.
- [Prebid Mobile iOS](https://github.com/prebid/prebid-mobile-ios) - iOS SDK counterpart supporting GAM bidding-only, Prebid-rendered, and mediation integration paths.
- [Prebid Cache](https://github.com/prebid/prebid-cache) - Reference key/value service that stores bid creatives and VAST XML so server-side bids can be fetched later by the ad server.
- [Prebid Universal Creative](https://github.com/prebid/prebid-universal-creative) - One ad-server creative that fetches and renders any winning Prebid bid, including AMP and in-app scenarios.
- [Prebid Server Endpoint Reference](https://docs.prebid.org/prebid-server/endpoints/pbs-endpoint-overview.html) - The full PBS API surface, from `/openrtb2/auction` and `/cookie_sync` through the admin and Prebid Cache endpoints.

---

## 🔍 Browser Extensions and Debugging Tools

Read the auction from the outside — these capture what the console alone will not show you.

- [Professor Prebid](https://github.com/prebid/professor-prebid) - Chrome extension that inspects live Prebid instances and reports ad units, bids, auction timeline, user IDs, and version details.
- [Professor Prebid User Guide](https://docs.prebid.org/tools/professor-prebid.html) - Official walkthrough of the extension's bid comparison, GAM console shortcut, CPM override, and creative overlay tools.
- [Headerbid Expert Patterns](https://github.com/prebid/headerbid-expert) - Community-maintained URL pattern file that drives Headerbid Expert's detection and timing of bidder responses.
- [Header Bidder Expert](https://github.com/prebid/header-bidder-expert) - Buildable Chrome and Firefox extension that lists the header bidding partners active on a page and the bids they returned.
- [Prebid Debugging Module](https://docs.prebid.org/dev-docs/modules/debugging.html) - Config-driven module that intercepts, mocks, or forces bid responses and validates first-party data before each auction.
- [Prebid.js Troubleshooting Guide](https://docs.prebid.org/troubleshooting/troubleshooting-guide.html) - Symptom-by-symptom guide to `pbjs_debug` output, adapter errors, missing bids, and rendering failures.
- [Ad Radar](https://github.com/hestiaAI/ad-radar) - Open-source browser extension that reads header bidding traffic to show which advertisers bid on you and at what price.
- [AuctionHouse](https://github.com/jldbc/AuctionHouse) - Chrome extension that records Prebid bid requests and exports bidder, CPM, and creative size as JSON; dormant since 2019 but still a readable reference.

---

## 🪪 User ID and Identity Modules

Cookie-free addressability is the hard part of modern wrappers — start with the module contract, then evaluate providers.

- [Prebid.js User ID Module](https://docs.prebid.org/dev-docs/modules/userId.html) - Core documentation for configuring ID submodules, storage, consent gating, and how IDs surface as `userId` and EIDs.
- [How to Add a User ID Submodule](https://docs.prebid.org/dev-docs/userId-module.html) - The `getId`, `decode`, and `eids` interface contract for publishing a Prebid.js identity module.
- [SharedID Documentation](https://docs.prebid.org/dev-docs/modules/userid-submodules/sharedid.html) - Docs for Prebid's free first-party `_pubcid` identifier, designed to survive ITP and be shared across adapters.
- [SharedID Server](https://github.com/prebid/shared-id) - Java and AWS implementation plus the `pubcid.js` client behind the sharedid.org first-party cookie namespace.
- [Prebid Identity Overview](https://docs.prebid.org/identity/prebid-identity.html) - How Prebid.js, Prebid Server, and Prebid Mobile handle IDs, EIDs, and consent-based suppression.
- [Identity Gatekeeper](https://github.com/prebid/identity-gatekeeper) - Prebid proposals and a working proof of concept for permissioning which identity signals reach which bidders.
- [ID5 API](https://github.com/id5io/id5-api.js) - Open-source JavaScript library for ID5's universal ID, shipped with a Prebid.js integration module.
- [Unified ID 2.0 Docs](https://github.com/IABTechLab/uid2docs) - Official UID2 documentation repository covering token generation, operators, SDKs, and Prebid integration.
- [UID2 Web Integrations](https://github.com/IABTechLab/uid2-web-integrations) - Reference web integration code for UID2, including the browser SDK and Prebid.js module wiring.
- [SWAN](https://github.com/SWAN-community/swan) - Open-source, privacy-preserving cross-domain identity network specification and implementation for publishers.

---

## 📊 Analytics, Monitoring and Latency Tools

If you cannot reconstruct the auction afterwards, you cannot defend the floor, the timeout, or the bidder mix.

- [Analytics Adapters for Prebid.js](https://docs.prebid.org/overview/analytics.html) - Index of the vendor analytics adapters that can be compiled into a build and enabled with `pbjs.enableAnalytics()`.
- [Generic Analytics Adapter](https://docs.prebid.org/dev-docs/modules/genericAnalyticsAdapter.html) - Publisher-owned adapter that batches any Prebid event to your own endpoint or handler, with sampling and per-event formatters.
- [How to Add an Analytics Adapter](https://docs.prebid.org/dev-docs/integrate-with-the-prebid-analytics-api.html) - Architecture and code template for endpoint and bundle adapters hooked into the Prebid event bus.
- [pbjs.getEvents() Reference](https://docs.prebid.org/dev-docs/publisher-api-reference/getEvents.html) - Canonical event schema from `auctionInit` through `bidTimeout` and `bidWon`, the foundation of any custom bidstream logger.
- [Prebid Server Analytics Adapters](https://docs.prebid.org/prebid-server/developers/pbs-build-an-analytics-adapter.html) - How to implement analytics modules for PBS-Go and PBS-Java, including the filesystem and log examples.
- [Blacklight](https://github.com/the-markup/blacklight-collector) - Open-source privacy inspector that loads a URL in headless Chrome and reports the ad-tech and tracking scripts it observes.
- [WebPageTest](https://github.com/catchpoint/WebPageTest) - Self-hostable performance testing platform for measuring the ad stack's cost in LCP, INP, and total blocking time.
- [Lighthouse](https://github.com/GoogleChrome/lighthouse) - Google's audit engine for measuring main-thread work, render-blocking scripts, and Core Web Vitals on ad-heavy pages.

---

## 🚀 Wrappers, Boilerplates and Starter Kits

Working starting points for the unglamorous parts: line items, key-values, build pipelines, and framework bindings.

- [dfp-prebid-setup](https://github.com/kmjennison/dfp-prebid-setup) - Generates Google Ad Manager line items and key-value targeting from a Prebid.js configuration file.
- [Prebid Line Item Manager](https://github.com/prebid/line-item-manager) - Prebid.org's tool for importing, auditing, and updating GAM line items against a live Prebid configuration.
- [Prebid.js GPT Integration Examples](https://github.com/prebid/Prebid.js/tree/master/integrationExamples/gpt) - Runnable HTML examples pairing Prebid.js with GPT, covering floor configuration, size mapping, and real-time data providers.
- [Prebid.js Packager](https://github.com/prebid/Prebid.js-packager) - Prebid's enterprise build service for compiling multiple Prebid.js bundles from shared module manifests.
- [Prebid Currency File](https://github.com/prebid/currency-file) - Auto-generated daily FX rates consumed by the Prebid.js currency module and Prebid Server.
- [Prebid Server on AWS](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws) - AWS Solutions guidance and infrastructure templates for deploying and operating Prebid Server.
- [ArcAds](https://github.com/washingtonpost/ArcAds) - Arc XP's GPT wrapper that standardizes slot configuration, targeting, and refresh while supporting Prebid.js and Amazon header bidding vendors.
- [PubFood](https://github.com/pubfood/pubfood) - Publisher-built open-source header bidding framework, now dormant but a clear reference for wrapper architecture.
- [react-advertising](https://github.com/KijijiCA/react-advertising) - React library for declaring display ad slots with pluggable demand providers instead of imperative GPT code.
- [react-ads](https://github.com/betancourtl/react-ads) - React components and hooks for wiring GPT, Prebid, and custom bidders into a component tree.
- [Google Publisher Tag Samples](https://github.com/googleads/google-publisher-tag-samples) - Google's official GPT samples, including auction-delay and targeting patterns used alongside Prebid.

---

## 📉 Price Floors, Timeouts and Optimization Guides

Floors and timeouts move revenue more than most wrapper rewrites — tune them with evidence, not defaults.

- [Prebid.js Price Floors Module](https://docs.prebid.org/dev-docs/modules/floors.html) - Schema 2 floor configuration, dynamic floor providers, and enforcement semantics for Prebid.js auctions.
- [Prebid Server Price Floors](https://docs.prebid.org/prebid-server/features/pbs-floors.html) - Server-side floor framework that caches floor data and resolves it into `imp.bidfloor` before adapters are called.
- [Prebid Timeouts](https://docs.prebid.org/features/timeouts.html) - Explains failsafe, auction, and timeout-adjustment layers, plus how to diagnose adapters that miss the window.
- [Prebid.js FAQ](https://docs.prebid.org/dev-docs/faq.html) - Official starting points for auction and failsafe timeouts, bid caching behavior, and GPT yield-group interactions.
- [pbjs.setConfig Reference](https://docs.prebid.org/dev-docs/publisher-api-reference/setConfig.html) - The full configuration surface: `bidderTimeout`, `priceGranularity`, `s2sConfig`, `userSync`, and RTD auction delays.
- [Publisher Sustainability Best Practices](https://docs.prebid.org/support/sustainability-publishers.html) - Prebid's guidance on build size, bidder count, analytics coverage, and user-sync hygiene.
- [Implementing Prebid Server: Q&A](https://clearcode.cc/blog/prebid-server-qa-implementation/) - Architecture interview covering hosted PBS design, auction flow, and the ad-server handoff.
- [Header Bidding Archive (Clearcode)](https://clearcode.cc/tag/header-bidding/) - Long-running engineering archive on client-side versus server-side auction design and waterfall dynamics.

---

## 📜 Specifications and Standards

Primary sources only — every field in a bid request traces back to one of these documents.

- [OpenRTB 2.x Specification](https://github.com/InteractiveAdvertisingBureau/openrtb2.x) - The current 2.6+ spec, its community extension framework, and protobuf definitions.
- [OpenRTB 3.0 Specification](https://github.com/InteractiveAdvertisingBureau/openrtb) - The layered 3.0 transaction model built on AdCOM, with request and response object definitions.
- [AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM) - The Advertising Common Object Model that supplies the domain layer and enum lists for OpenRTB 2.6 and 3.0.
- [OpenRTB Data Models](https://github.com/InteractiveAdvertisingBureau/openrtb-model) - Machine-readable data models for OpenRTB 2.x and 3.0, useful for code generation and validation.
- [ads.txt Specification](https://iabtechlab.com/ads-txt/) - The authoritative ads.txt and app-ads.txt specification for declaring authorized sellers of inventory.
- [sellers.json and SupplyChain](https://iabtechlab.com/sellers-json/) - Specifications and implementation guidance for verifying who sells an impression and how it traveled through the chain.
- [Curated Audiences (SDA)](https://iabtechlab.com/sda/) - The seller-defined audiences framework, renamed Curated Audiences, for passing publisher-owned segments in OpenRTB.
- [IAB Tech Lab Taxonomies](https://github.com/InteractiveAdvertisingBureau/Taxonomies) - Machine-readable content, audience, and ad-product taxonomies with IDs, used for `cattax` and `segtax` fields.
- [Global Privacy Platform](https://github.com/InteractiveAdvertisingBureau/Global-Privacy-Platform) - The GPP specification that consolidates regional privacy signals into a single consent string for the bidstream.
- [TCF Specification](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework) - IAB Europe's Transparency and Consent Framework technical specs, including the TC string format.
- [iabtcf-es](https://github.com/InteractiveAdvertisingBureau/iabtcf-es) - Official TypeScript and JavaScript library for encoding, decoding, and validating TCF v2 consent strings.
- [ads.txt Crawler](https://github.com/InteractiveAdvertisingBureau/adstxtcrawler) - Reference Python crawler that fetches and parses ads.txt files at scale.
- [Trusted Server](https://github.com/IABTechLab/trusted-server) - IAB Tech Lab's open-source edge reverse proxy that gives publishers a first-party ID and runs auctions at the CDN layer.
- [rtblint](https://github.com/aleksUIX/rtblint) - OpenRTB linter that validates 2.x bid requests and responses against versioned schemas and spec rules.
- [OpenRTB Go Types](https://github.com/prebid/openrtb) - Maintained Go types and enums for OpenRTB 2.x, 3.0, AdCOM, and Native, used by Prebid Server.

---

## 💬 Communities and Newsletters

Where wrapper regressions get reported first, and where the reasoning behind the specs is argued out.

- [Prebid Slack](https://prebid.slack.com) - Prebid.org's invite-gated Slack workspace where adapter reviews, release notes, and PBS operations are discussed.
- [Prebid Support](https://docs.prebid.org/support/) - Official support routes, including the Ad Ops Slack `#HeaderBidding` channel, GitHub issues, and contact forms.
- [r/adops](https://www.reddit.com/r/adops/) - Practitioner subreddit for floors, GAM line items, waterfall debugging, and SSP comparisons.
- [Stack Overflow: prebid.js](https://stackoverflow.com/questions/tagged/prebid.js) - Tagged Q&A for concrete implementation errors in Prebid.js integrations.
- [Prebid Blog](https://prebid.org/blog/) - Release notes, project announcements, and engineering posts from the Prebid.org community.
- [AdExchanger](https://www.adexchanger.com/) - Programmatic industry reporting on auctions, identity, and supply-path economics.
- [AdMonsters](https://www.admonsters.com/) - Ad ops community and newsletter covering GAM, yield management, and wrapper operations.
- [Google Ads Developer Blog](https://ads-developers.googleblog.com/) - Google's developer blog covering Ad Manager API, GPT, and Ads API changes.

---

## 🤝 Contributing

PRs are welcome — this list only stays useful if entries stay accurate.

- **Keep it open** — prefer an open-source repository, an official specification, or a first-party developer tool over a vendor landing page.
- **One sentence, technical, neutral** — describe what the thing does and where it sits in the auction, not why it is great.
- **Verify the link** — every URL must resolve without a login wall, and archived or dormant projects should be labeled as such.
- **Follow the format** — copy the template below exactly, including the separating hyphen.
- **One entry per PR** — state what makes the addition canonical enough to outlive the next release cycle.

```markdown
- [Resource Name](https://url) - Concise, technical 1-sentence description.
```

---

## 📄 License

Released under [CC0 1.0 Universal](./LICENSE) — the list is dedicated to the public domain, so copy, remix, and redistribute it without attribution.

Prebid, OpenRTB, ads.txt, sellers.json, and related names are the property of their respective owners; links are provided for identification only.
