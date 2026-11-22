<div align="center">

[![awesome-header-bidding](image/awesome-header-bidding.png)](https://github.com/adops-tool/awesome-header-bidding/pulls)

[![animated-line](https://github.com/readme-SVG/animated-line/blob/main/STORAGE/line-svg-3D444D.svg)](https://github.com/readme-SVG/animated-line) <!-- -SVG-Line- -->

**A curated, engineering-first index of the open-source header bidding stack — wrappers, auction servers, debuggers, identity and consent modules, floor tooling, specifications, and the reference implementations that make programmatic auctions legible and measurable.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

</div>

> Each entry is marked with the kind of resource it is: ![github](image/alg_R.png) open-source repository, ![web](image/alg_I.png) documentation, specification, or hosted tool. Dormant and archived projects are kept when they still explain an architecture — they are labeled as such.

## Table of Contents

- [Core Auction Engines and Wrappers](#core-auction-engines-and-wrappers)
- [Debugging, Extensions and Local Tooling](#debugging-extensions-and-local-tooling)
- [Ad Server Integration and Line Item Automation](#ad-server-integration-and-line-item-automation)
- [Identity, Consent and Privacy](#identity-consent-and-privacy)
- [Analytics, Monitoring and Performance](#analytics-monitoring-and-performance)
- [Floors, Timeouts and Yield Optimization](#floors-timeouts-and-yield-optimization)
- [Video, CTV and SSAI Tooling](#video-ctv-and-ssai-tooling)
- [Open Ad Servers, DSPs and Reference Implementations](#open-ad-servers-dsps-and-reference-implementations)
- [Specifications and Standards](#specifications-and-standards)
- [Documentation, Learning and Community](#documentation-learning-and-community)
- [Contributing](#contributing)
- [License](#license)

---

## Core Auction Engines and Wrappers

*The code that runs the auction, from the on-page wrapper through the server-side engine to the creative that renders the winner.*

### Client-Side Wrappers and Build Tooling

![github](image/alg_R.png) [Prebid.js](https://github.com/prebid/Prebid.js) - The de facto client-side header bidding wrapper: runs a parallel auction across its bid adapters and writes winning bids into ad server key-values.

![github](image/alg_R.png) [Prebid.js GPT integration examples](https://github.com/prebid/Prebid.js/tree/master/integrationExamples/gpt) - Runnable HTML pages pairing Prebid.js with GPT, covering floors, size mapping, and real-time data providers.

![github](image/alg_R.png) [prebid-js-build-generator](https://github.com/prebid/prebid-js-build-generator) - The build backend that compiles the custom Prebid.js bundles served from the prebid.org download page.

![github](image/alg_R.png) [Prebid.js Packager](https://github.com/prebid/Prebid.js-packager) - Self-hostable service for compiling multiple Prebid.js bundles from shared module manifests; dormant since 2022.

![github](image/alg_R.png) [EdgeKit](https://github.com/AirGrid/edgekit) - Client-side auction and monetisation library from AirGrid; archived in 2024 but a clean reference for a wrapper written in TypeScript.

![github](image/alg_R.png) [PubFood](https://github.com/pubfood/pubfood) - Publisher-built open-source header bidding framework; unmaintained, still useful for comparing wrapper architectures.

![web](image/alg_I.png) [Prebid.js Download](https://prebid.org/download.html) - Pick a Prebid.js version and a module set and get a compiled bundle back.

![web](image/alg_I.png) [Prebid.js Module Index](https://docs.prebid.org/dev-docs/modules/) - Catalog of recommended, general, and vendor-specific modules with build commands and configuration references.

![web](image/alg_I.png) [Prebid Module Rules](https://docs.prebid.org/dev-docs/module-rules.html) - The naming, privacy, and code rules a Prebid.js or Prebid Server module must satisfy to be listed on prebid.org.

![web](image/alg_I.png) [Prebid.js Getting Started](https://docs.prebid.org/dev-docs/getting-started.html) - Setup walkthrough from loading the library to reading the first auction in the console.

![web](image/alg_I.png) [Ad Unit Reference](https://docs.prebid.org/dev-docs/adunit-reference.html) - Field-by-field reference for ad unit, mediaTypes, and ortb2Imp configuration.

![web](image/alg_I.png) [pbjs.setConfig Reference](https://docs.prebid.org/dev-docs/publisher-api-reference/setConfig.html) - The full configuration surface: `bidderTimeout`, `priceGranularity`, `s2sConfig`, `userSync`, and RTD auction delays.

![web](image/alg_I.png) [How to Add a Prebid.js Bid Adapter](https://docs.prebid.org/dev-docs/bidder-adaptor.html) - Adapter contract, required parameters, and the review rules a new Prebid.js bidder must satisfy.

![web](image/alg_I.png) [Prebid.js Bidder List](https://docs.prebid.org/dev-docs/bidders.html) - Every supported adapter with its media types, module requirements, and params.

![web](image/alg_I.png) [How to Add Video Support to a Bidder Adapter](https://docs.prebid.org/dev-docs/add-video-support-to-an-existing-bidder-adaptor.html) - What an existing display adapter must add to return VAST and ad pod responses.

![web](image/alg_I.png) [Conditional Ad Units](https://docs.prebid.org/dev-docs/conditional-ad-units.html) - Label-driven ad unit filtering, the mechanism behind responsive and device-specific auctions.

![web](image/alg_I.png) [Testing Prebid.js](https://docs.prebid.org/dev-docs/testing-prebid.html) - Prebid's own test requirements, including the coverage threshold enforced on adapter pull requests.

### Server-Side Auction Engines

![github](image/alg_R.png) [Prebid Server (Go)](https://github.com/prebid/prebid-server) - High-throughput Go implementation of the Prebid Server auction engine for web, AMP, mobile, video, and CTV requests.

![github](image/alg_R.png) [Prebid Server (Java)](https://github.com/prebid/prebid-server-java) - Spring-based Prebid Server implementation with a modular hook framework, commonly deployed where Spring and hook-based modules are preferred.

![github](image/alg_R.png) [Prebid Cache](https://github.com/prebid/prebid-cache) - Reference key/value service that stores bid creatives and VAST XML so server-side bids can be fetched later by the ad server.

![github](image/alg_R.png) [Prebid Cache (Java)](https://github.com/prebid/prebid-cache-java) - Java implementation of the Prebid Cache endpoints for stacks already running PBS-Java.

![github](image/alg_R.png) [Prebid Universal Creative](https://github.com/prebid/prebid-universal-creative) - One ad-server creative that fetches and renders any winning Prebid bid, including AMP and in-app scenarios.

![github](image/alg_R.png) [Prebid User Sync Utilities](https://github.com/prebid/user-sync) - Builds the `load_cookie.html` endpoints used to initiate bidder cookie syncs from Prebid Server in AMP flows.

![github](image/alg_R.png) [RapidPrebidServer](https://github.com/RapidCodeLab/rapid-prebid-server) - Independent Go server-to-server header bidding engine and a compact read on how a lightweight PBS-style auction is structured; dormant since 2023.

![github](image/alg_R.png) [Dynamic Traffic Engine](https://github.com/IABTechLab/DynamicTrafficEngine) - IAB Tech Lab traffic shaping layer that samples, filters, and routes OpenRTB bid traffic between buyers and sellers with real-time configuration.

![github](image/alg_R.png) [Prebid Server on AWS](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws) - AWS Solutions guidance and infrastructure templates for deploying and operating Prebid Server.

![github](image/alg_R.png) [Trusted Server](https://github.com/IABTechLab/trusted-server) - Rust edge reverse proxy that gives publishers a first-party URL space, supports Prebid Server at the CDN layer, and adds ID and ads.cert handling.

![web](image/alg_I.png) [Prebid Server Endpoint Overview](https://docs.prebid.org/prebid-server/endpoints/pbs-endpoint-overview.html) - The full PBS API surface, from `/openrtb2/auction` and `/cookie_sync` through the admin and Prebid Cache endpoints.

![web](image/alg_I.png) [PBS Auction Endpoint Reference](https://docs.prebid.org/prebid-server/endpoints/openrtb2/pbs-endpoint-auction.html) - Request and response shape of `/openrtb2/auction`, including the `ext.prebid` blocks PBS adds.

![web](image/alg_I.png) [PBS AMP Endpoint Reference](https://docs.prebid.org/prebid-server/endpoints/openrtb2/pbs-endpoint-amp.html) - How AMP requests are validated and mapped onto stored requests.

![web](image/alg_I.png) [PBS Stored Requests](https://docs.prebid.org/prebid-server/features/pbs-storedreqs.html) - Server-side OpenRTB blocks merged into mobile and AMP requests, with data source and merge semantics.

![web](image/alg_I.png) [PBS Caching](https://docs.prebid.org/prebid-server/features/pbs-caching.html) - When and why PBS moves bids into cache, plus the response caching and winning-bid caching controls.

![web](image/alg_I.png) [PBS Modules Index](https://docs.prebid.org/prebid-server/pbs-modules/) - Index of server-side modules — hooks for bidding, privacy, and analytics that are compiled into PBS-Go and PBS-Java.

![web](image/alg_I.png) [How to Add a PBS Module (Go)](https://docs.prebid.org/prebid-server/developers/add-a-module-go.html) - Hook framework, module registration, and test expectations for PBS-Go modules.

![web](image/alg_I.png) [How to Add a Prebid Server Adapter](https://docs.prebid.org/prebid-server/developers/add-new-bidder-go.html) - The full checklist for shipping a bidder into PBS-Go, from OpenRTB mapping to adapter tests.

![web](image/alg_I.png) [Installing Prebid Server (Go)](https://docs.prebid.org/prebid-server/developers/installing-go.html) - Build, configuration, and startup of a local PBS-Go instance.

![web](image/alg_I.png) [Installing Prebid Server (Java)](https://docs.prebid.org/prebid-server/developers/installing-java.html) - Equivalent setup path for the Spring-based PBS-Java build.

![web](image/alg_I.png) [Prebid Server Bidder Params](https://docs.prebid.org/dev-docs/pbs-bidders.html) - Per-bidder parameter reference for server-side requests.

![web](image/alg_I.png) [Hosted Prebid Servers](https://prebid.org/product-suite/managed-services/) - Prebid.org members that install and operate Prebid and Prebid Server on a publisher's behalf.

![web](image/alg_I.png) [Prebid Server Cookie Sync](https://docs.prebid.org/prebid-server/developers/pbs-cookie-sync.html) - Bidders' sync endpoints and how to initiate a sync manually for debugging.

![web](image/alg_I.png) [Prebid.js s2sConfig Reference](https://docs.prebid.org/dev-docs/modules/prebidServer.html) - How the client calls PBS: account, stored requests, `disableBidCache`, and multi-format flags.

### Rendering, Caching and Creative Containers

![web](image/alg_I.png) [Prebid Universal Creative Overview](https://docs.prebid.org/overview/prebid-universal-creative.html) - The rendering routines PUC uses to pull a cached ad ID and display display, video, AMP, or in-app winners.

![web](image/alg_I.png) [Renderer Reference](https://docs.prebid.org/dev-docs/renderer.html) - How Prebid renderers take over display of a bid, the mechanism behind outstream and in-renderer video.

![web](image/alg_I.png) [Safe Rendering Module](https://docs.prebid.org/dev-docs/modules/safeRendering.html) - `pbjs.renderBid()` rendering inside an iframe that cannot reach the publisher page, plus the SafeFrame opt-out controls.

![web](image/alg_I.png) [Native Rendering Module](https://docs.prebid.org/dev-docs/modules/nativeRendering.html) - Renders native bids through `pbjs.renderAd()` or ad-server dynamic creatives.

![web](image/alg_I.png) [JavaScript Dynamic Creatives](https://docs.prebid.org/adops/js-dynamic-creative.html) - Ad-server creative snippet that lets Prebid render the winning bid from the page instead of a fixed tag.

![web](image/alg_I.png) [Show Multi-Format Ads](https://docs.prebid.org/dev-docs/show-multi-format-ads.html) - Combining banner, video, and native demand in one auction and one ad server setup.

![web](image/alg_I.png) [Show Outstream Video Ads](https://docs.prebid.org/dev-docs/show-outstream-video-ads.html) - Outstream setup with a Prebid renderer and ad-server creative.

![web](image/alg_I.png) [Show Native Ads](https://docs.prebid.org/dev-docs/show-native-ads.html) - Native asset configuration and ad-server handoff for Prebid native demand.

![web](image/alg_I.png) [Show Prebid Ads on AMP Pages](https://docs.prebid.org/dev-docs/show-prebid-ads-on-amp-pages.html) - The AMP data provider, its restrictions, and the PBS stored-request requirements behind it.

![web](image/alg_I.png) [Show Long-Form Video with GAM](https://docs.prebid.org/dev-docs/show-long-form-video-with-gam.html) - Ad pod and category translation trafficking flow for long-form video.

![github](image/alg_R.png) [Prebid Outstream Renderer](https://github.com/prebid/prebid-outstream) - Prebid.org's open-source outstream player used as the renderer for video bids in display slots.

![github](image/alg_R.png) [In-Renderer JS](https://github.com/hogekai/in-renderer-js) - Open-source Prebid renderer for in-renderer (formerly outstream) integrations; archived in 2026.

![github](image/alg_R.png) [Prebid Video Cache Redirector](https://github.com/prebid/prebid-video-cache-redirector) - Small redirect service that keeps ad-server video creatives pointed at the right Prebid Cache URL; dormant since 2019.

![github](image/alg_R.png) [Cross-Player Prebid Component](https://github.com/prebid/cross-player-prebid-component) - `postMessage`-based component that runs the Prebid auction and hands the result to any third-party video player; dormant since 2020.

![github](image/alg_R.png) [SHARC](https://github.com/IABTechLab/SHARC) - Secure HTML Ad Richmedia Container: a sandboxed communication API between page and creative, proposed as a SafeFrame and MRAID successor.

![github](image/alg_R.png) [SafeFrame](https://github.com/InteractiveAdvertisingBureau/safeframe) - Reference implementation of the iframe container that lets a creative request expansion or resize under publisher control.

![github](image/alg_R.png) [UCID](https://github.com/IABTechLab/ucid) - Universal Creative Identification Framework, an open specification for fingerprinting creatives across the supply chain.

### Mobile, CTV and In-App SDKs

![github](image/alg_R.png) [Prebid Mobile Android](https://github.com/prebid/prebid-mobile-android) - Android SDK that requests bids from Prebid Server and renders them through GAM, AdMob, AppLovin MAX, or a custom ad server.

![github](image/alg_R.png) [Prebid Mobile iOS](https://github.com/prebid/prebid-mobile-ios) - iOS SDK counterpart supporting GAM bidding-only, Prebid-rendered, and mediation integration paths.

![github](image/alg_R.png) [Prebid Mobile Flutter](https://github.com/prebid/prebid-mobile-flutter) - Prebid.org's Flutter plugin wrapping the Prebid Mobile SDK; incubating, with the repository as the only documentation for now.

![github](image/alg_R.png) [prebid-mobile-flutter (community)](https://github.com/thanhhaidev/prebid-mobile-flutter) - Unofficial Flutter plugin covering Prebid rendering, the Original API, GAM, and AdMob paths.

![github](image/alg_R.png) [react-native-ad-manager](https://github.com/narcitymedia/react-native-ad-manager) - React Native wrapper around the Google Ad Manager SDKs, the usual host for Prebid Mobile mediation; dormant since 2020.

![github](image/alg_R.png) [Epom Prebid Mobile demo apps](https://github.com/epom/epom-prebid-mobile-demo) - Reference iOS and Android apps selling in-app inventory through Epom Ad Server with Prebid Mobile.

![web](image/alg_I.png) [Prebid Mobile Documentation](https://docs.prebid.org/prebid-mobile/) - SDK integration guides for both platforms, from initialization to ad server setup.

![web](image/alg_I.png) [Getting Started with Prebid Mobile](https://docs.prebid.org/prebid-mobile/prebid-mobile-getting-started.html) - The ad-ops and developer steps needed before the first in-app auction runs.

![web](image/alg_I.png) [Prebid Mobile Video Guide](https://docs.prebid.org/prebid-mobile/prebid-mobile-video.html) - In-app rewarded, interstitial, and native video flows and their ad server requirements.

![web](image/alg_I.png) [Prebid Mobile Privacy Regulation Guide](https://docs.prebid.org/prebid-mobile/prebid-mobile-privacy-regulation.html) - How GDPR, CCPA, and other regimes apply to in-app bidding, and which SDK APIs handle consent.

![web](image/alg_I.png) [Mobile Ad Operations Guide](https://docs.prebid.org/adops/mobile-adops.html) - Trafficking differences between web and in-app header bidding, including SDK caches.

![web](image/alg_I.png) [GAM Line Item Setup for Mobile Rendering](https://docs.prebid.org/adops/mobile-rendering-gam-line-item-setup.html) - Ad-server configuration for the rendering-in-app path rather than the bidding-only path.

![web](image/alg_I.png) [Prebid Mobile Download](https://docs.prebid.org/prebid-mobile/prebid-mobile-download.html) - Current SDK artifacts and adapter packages published by the mobile teams.

---

## Debugging, Extensions and Local Tooling

*Reading the auction from the outside: extensions that inspect live instances, modules that mock or force responses, and the guides the maintainers actually use.*

### Browser Extensions and In-Page Inspectors

![github](image/alg_R.png) [Professor Prebid](https://github.com/prebid/professor-prebid) - Chrome extension that inspects live Prebid instances and reports ad units, bids, auction timeline, user IDs, and version details.

![github](image/alg_R.png) [Headerbid Expert Patterns](https://github.com/prebid/headerbid-expert) - Community-maintained URL pattern file that drives Headerbid Expert's detection and timing of bidder responses.

![github](image/alg_R.png) [Header Bidder Expert](https://github.com/prebid/header-bidder-expert) - Buildable Chrome and Firefox extension that lists the header bidding partners active on a page and the bids they returned.

![github](image/alg_R.png) [AuctionHouse](https://github.com/jldbc/AuctionHouse) - Chrome extension that records Prebid bid requests and exports bidder, CPM, and creative size as JSON; dormant since 2019 but still a readable reference.

![github](image/alg_R.png) [Ad Radar](https://github.com/hestiaAI/ad-radar) - Open-source browser extension that reads header bidding traffic to show which advertisers bid on you and at what price.

![github](image/alg_R.png) [Bazaar](https://github.com/gmodena/bazaar) - WebExtension that collects Prebid.js requests for offline inspection; dormant since 2021.

![github](image/alg_R.png) [hb-finder](https://github.com/kasparsd/hb-finder) - Small detection script that reports which header bidding solutions a page is running; dormant since 2017.

![github](image/alg_R.png) [Ad Block Detection](https://github.com/InteractiveAdvertisingBureau/AdBlockDetection) - IAB's reference detection scripts for telling when the ad stack never got a chance to run; dormant since 2019.

![github](image/alg_R.png) [self-adint](https://github.com/genaforvena/self-adint) - Reads your own advertising profile from the demand side by inspecting what an RTB bid request carries about one device.

![web](image/alg_I.png) [Professor Prebid User Guide](https://docs.prebid.org/tools/professor-prebid.html) - Official walkthrough of the extension's bid comparison, GAM console shortcut, CPM override, and creative overlay tools.

![web](image/alg_I.png) [Professor Prebid Video Guide](https://docs.prebid.org/tools/prof-prebid-video.html) - The same tools demonstrated on a live page.

![web](image/alg_I.png) [Prebid Debugging Module](https://docs.prebid.org/dev-docs/modules/debugging.html) - Config-driven module that intercepts, mocks, or forces bid responses and validates first-party data before each auction.

![web](image/alg_I.png) [DevTools MCP Module](https://docs.prebid.org/dev-docs/modules/devtoolsMcp.html) - Exposes live Prebid.js state — auctions, bids, events, modules, config — as Chrome DevTools third-party developer tools, so an agent or the MCP client can query them.

### Diagnostics, Logs and Test Harnesses

![web](image/alg_I.png) [Prebid.js Troubleshooting Guide](https://docs.prebid.org/troubleshooting/troubleshooting-guide.html) - Symptom-by-symptom guide to `pbjs_debug` output, adapter errors, missing bids, and rendering failures.

![web](image/alg_I.png) [Prebid.js Troubleshooting Guide (developer copy)](https://docs.prebid.org/dev-docs/prebid-troubleshooting-guide.html) - The same checklist written for developers, with the console commands for each step.

![web](image/alg_I.png) [Prebid Server Troubleshooting](https://docs.prebid.org/troubleshooting/pbs-troubleshooting.html) - Diagnosing no-bid, timeout, and account-configuration problems on the server side.

![web](image/alg_I.png) [Common Issues](https://docs.prebid.org/dev-docs/common-issues.html) - Recurring misconfigurations and the observable symptoms that identify them.

![web](image/alg_I.png) [Prebid.js FAQ](https://docs.prebid.org/dev-docs/faq.html) - Official starting points for auction and failsafe timeouts, bid caching behavior, and GPT yield-group interactions.

![web](image/alg_I.png) [pbjs.getEvents() Reference](https://docs.prebid.org/dev-docs/publisher-api-reference/getEvents.html) - Canonical event schema from `auctionInit` through `bidTimeout` and `bidWon`, the foundation of any custom bidstream logger.

![web](image/alg_I.png) [pbjs.getAdserverTargeting() Reference](https://docs.prebid.org/dev-docs/publisher-api-reference/getAdserverTargeting.html) - Reads the key-values Prebid wrote for each slot, the quickest way to confirm what the ad server will see.

![web](image/alg_I.png) [pbjs.getAllWinningBids() Reference](https://docs.prebid.org/dev-docs/publisher-api-reference/getAllWinningBids.html) - Lists bids that rendered in the current page view, used when reconciling client-side wins against ad-server delivery.

![web](image/alg_I.png) [pbjs.installedModules() Reference](https://docs.prebid.org/dev-docs/publisher-api-reference/installedModules.html) - Reports which modules are actually compiled into the bundle you loaded — the first check when behavior and docs disagree.

![github](image/alg_R.png) [ccinnOpenRTB](https://github.com/whiteCcinn/ccinnOpenRTB) - Native macOS simulator that renders pasted OpenRTB 2.x and 3.0 bid responses so you can see what a creative will do.

![github](image/alg_R.png) [Prebid Integration Monitor](https://github.com/prebid/prebid-integration-monitor) - Prebid.org harness for monitoring a Prebid integration at runtime, built in TypeScript with Vitest; incubating.

---

## Ad Server Integration and Line Item Automation

*Everything between a winning bid and a served impression: key-values, line items, trafficking decisions, and the libraries that automate them.*

### Key-Values, Trafficking and Ad Server Mechanics

![web](image/alg_I.png) [Ad Server Key Values](https://docs.prebid.org/features/adServerKvps.html) - Which key-values Prebid sets, how they are scoped, and how the ad server uses them to pick a creative.

![web](image/alg_I.png) [Key Values in Depth](https://docs.prebid.org/adops/key-values.html) - The ad-ops view of the same mechanism: deal IDs, category, size, and the caching ID.

![web](image/alg_I.png) [Price Granularity](https://docs.prebid.org/adops/price-granularity.html) - How bucket definitions change both yield and line item count, with the density trade-off spelled out.

![web](image/alg_I.png) [Send All Bids vs Top Price](https://docs.prebid.org/adops/send-all-vs-top-price.html) - The two auction models, their effect on bidder behavior, and when each is appropriate.

![web](image/alg_I.png) [Ad Server Integration](https://docs.prebid.org/adops/ad-server-integration.html) - The generic integration contract any ad server must meet to consume Prebid bids.

![web](image/alg_I.png) [Creative Considerations](https://docs.prebid.org/adops/creative-considerations.html) - Setting up creatives so display, video, and native formats all render correctly.

![web](image/alg_I.png) [Header Bidding Trafficking Step by Step](https://docs.prebid.org/adops/gam-hbt-step-by-step.html) - Header bidding trafficking in GAM as an alternative to per-price line items.

![web](image/alg_I.png) [How to Simplify Line Item Setup](https://docs.prebid.org/overview/how-to-simplify-line-item-setup.html) - The options Prebid recommends for cutting line item sprawl, from price buckets to dynamic creatives.

![web](image/alg_I.png) [Ad Ops Planning Guide](https://docs.prebid.org/adops/adops-planning-guide.html) - Pre-launch decisions an ad ops team needs to settle before the first auction runs.

![web](image/alg_I.png) [Before You Start](https://docs.prebid.org/adops/before-you-start.html) - Prerequisites and the organizational context behind the technical setup.

![web](image/alg_I.png) [Deals in the Ad Server](https://docs.prebid.org/adops/deals.html) - How PMP deals flow through key-values and how to traffic them.

![web](image/alg_I.png) [Custom Deal Rendering](https://docs.prebid.org/features/customDealRendering.html) - Letting Prebid render deal creatives instead of the ad server, and the constraints that come with it.

![web](image/alg_I.png) [Prebid Ad Slot and GPID](https://docs.prebid.org/features/pbAdSlot.html) - The stable slot identifier bidders and the ad server match on; what breaks when it is missing.

![web](image/alg_I.png) [GPT Pre-Auction Module](https://docs.prebid.org/dev-docs/modules/gpt-pre-auction.html) - Reads GPT slot definitions before the auction to generate GPIDs and slot-level data.

![web](image/alg_I.png) [Interstitial Ads](https://docs.prebid.org/features/InterstitialAds.html) - The `adUnits` mechanics behind full-screen interstitial demand and its opt-out handling.

![web](image/alg_I.png) [What is Post-Bid?](https://docs.prebid.org/overview/what-is-post-bid.html) - The competing model, where demand bids after the ad server has declined a line item.

### Google Ad Manager API and Client Libraries

![web](image/alg_I.png) [Google Publisher Tag Reference](https://developers.google.com/publisher-tag/reference) - The authoritative `googletag` API reference for defining slots, targeting, and refresh.

![web](image/alg_I.png) [Google Ad Manager API](https://developers.google.com/ad-manager/api) - Entry point to the SOAP and REST surfaces used to automate orders, line items, and creatives.

![github](image/alg_R.png) [Google Publisher Tag Samples](https://github.com/googleads/google-publisher-tag-samples) - Google's official GPT samples, including auction-delay and targeting patterns used alongside Prebid.

![github](image/alg_R.png) [Google Publisher Tag Playground](https://github.com/googleads/google-publisher-tag-playground) - Interactive playground for writing and running the official GPT samples in the browser.

![github](image/alg_R.png) [Google Publisher Tag Types](https://github.com/googleads/google-publisher-tag-types) - Generated TypeScript definitions for GPT, which makes wrapper code type-checkable.

![github](image/alg_R.png) [Google Ad Manager PHP Client](https://github.com/googleads/googleads-php-lib) - Official PHP client library for the Ad Manager SOAP API.

![github](image/alg_R.png) [Google Ad Manager Java Client](https://github.com/googleads/googleads-java-lib) - Official Java client library for the Ad Manager SOAP API.

![github](image/alg_R.png) [Google Ad Manager .NET Client](https://github.com/googleads/googleads-dotnet-lib) - Official .NET client library for the Ad Manager SOAP API.

![github](image/alg_R.png) [Google Ad Manager Ruby Client](https://github.com/googleads/google-api-ads-ruby) - Official Ruby client libraries for the Ad Manager SOAP API.

![github](image/alg_R.png) [guardian/google-admanager-api](https://github.com/guardian/google-admanager-api) - TypeScript client for the Google Ad Manager API written and maintained by The Guardian.

![github](image/alg_R.png) [Niurmiguel/google-admanager-api](https://github.com/Niurmiguel/google-admanager-api) - Node.js client library for the Ad Manager API with a typed, promise-based interface.

![github](image/alg_R.png) [thewizarodofoz/google-ad-manager-api](https://github.com/thewizarodofoz/google-ad-manager-api) - Modern TypeScript wrapper around the Ad Manager API with schema-derived request and response types; dormant since 2023.

### Line Item and Targeting Automation

![github](image/alg_R.png) [dfp-prebid-setup](https://github.com/kmjennison/dfp-prebid-setup) - Generates Google Ad Manager line items and key-value targeting from a Prebid.js configuration file, deployable as a Cloud Function.

![github](image/alg_R.png) [Prebid Line Item Manager](https://github.com/prebid/line-item-manager) - Prebid.org's tool for importing, auditing, and updating GAM line items against a live Prebid configuration.

![github](image/alg_R.png) [dfp-prebid-lineitems](https://github.com/Insideall/dfp-prebid-lineitems) - PHP script that creates and updates Prebid line items in DFP from a price bucket definition; dormant since 2022.

![web](image/alg_I.png) [Prebid Line Item Manager Guide](https://docs.prebid.org/tools/line-item-manager.html) - Deployment and usage notes for the manager, including the credentials it needs.

![web](image/alg_I.png) [Line Item Creation Reference](https://docs.prebid.org/adops/line-item-creation.html) - The manual version: bucket math, targeting, and creative assignment per price.

![github](image/alg_R.png) [Ad Refresh Control](https://github.com/10up/Ad-Refresh-Control) - WordPress plugin that enables Active View refresh for GAM placements without touching page code.

![github](image/alg_R.png) [google-ad-manager-mcp](https://github.com/MatiousCorp/google-ad-manager-mcp) - MCP server exposing GAM campaigns, orders, line items, and creatives to an agent client.

### Framework, CMS and Player Bindings

![github](image/alg_R.png) [react-advertising](https://github.com/KijijiCA/react-advertising) - React library for declaring display ad slots with pluggable demand providers instead of imperative GPT code.

![github](image/alg_R.png) [react-ads](https://github.com/betancourtl/react-ads) - React components and hooks for wiring GPT, Prebid, and custom bidders into a component tree; dormant since 2023.

![github](image/alg_R.png) [react-gpt](https://github.com/nfl/react-gpt) - NFL's React component for Google Publisher Tag, covering slot definition, targeting, and refresh.

![github](image/alg_R.png) [goopubtag](https://github.com/IainMcHugh/goopubtag) - React library wrapping Google Publisher Tag with slot and targeting components.

![github](image/alg_R.png) [vue-advertising](https://github.com/storipress/vue-advertising) - Vue components for programmatic ad-ops integration; archived in 2025.

![github](image/alg_R.png) [react-prebid-adunit](https://github.com/rafaelverger/react-prebid-adunit) - React component that wraps an AdUnit container around a Prebid.js slot; dormant since 2023.

![github](image/alg_R.png) [10up ads-txt Manager](https://github.com/10up/ads-txt) - WordPress plugin for maintaining `ads.txt` and `app-ads.txt` files from the admin UI.

![github](image/alg_R.png) [Prebid.js Brightcove Plugin](https://github.com/prebid/prebid-js-plugin-brightcove) - Plugin that runs a Prebid video auction for a Brightcove player; dormant since 2020.

### Publisher Production Wrappers

![github](image/alg_R.png) [ArcAds](https://github.com/washingtonpost/ArcAds) - Arc XP's GPT wrapper that standardizes slot configuration, targeting, and refresh while supporting Prebid.js and Amazon header bidding vendors.

![github](image/alg_R.png) [Discourse Ad Plugin](https://github.com/discourse/discourse-adplugin) - Official forum ad plugin with adapters for AdSense, DFP, and other networks; archived in 2025.
---

## Identity, Consent and Privacy

*Addressability without cookies and the consent gates in front of it — module contracts, open identifiers, and the control planes that suppress what should not be sent.*

### Identifier Frameworks and ID Modules

![web](image/alg_I.png) [Prebid.js User ID Module](https://docs.prebid.org/dev-docs/modules/userId.html) - Core documentation for configuring ID submodules, storage, consent gating, and how IDs surface as `userId` and EIDs.

![web](image/alg_I.png) [How to Add a User ID Submodule](https://docs.prebid.org/dev-docs/userId-module.html) - The `getId`, `decode`, and `eids` interface contract for publishing a Prebid.js identity module.

![web](image/alg_I.png) [Prebid Identity Overview](https://docs.prebid.org/identity/prebid-identity.html) - How Prebid.js, Prebid Server, and Prebid Mobile handle IDs, EIDs, and consent-based suppression.

![web](image/alg_I.png) [SharedID Documentation](https://docs.prebid.org/identity/sharedid.html) - Prebid's free first-party `_pubcid` identifier, designed to survive ITP and be shared across adapters.

![github](image/alg_R.png) [SharedID Server](https://github.com/prebid/shared-id) - Java and AWS implementation behind the sharedid.org first-party cookie namespace.

![github](image/alg_R.png) [pubcid.js](https://github.com/prebid/Shared-id-v2) - The client library that mints and reads the site-scoped SharedID cookie; no cross-domain syncing.

![github](image/alg_R.png) [sharedid-wordpress](https://github.com/prebid/sharedid-wordpress) - WordPress plugin that injects the SharedID (formerly PubCommon ID) client; dormant since 2020.

![github](image/alg_R.png) [ID5 API](https://github.com/id5io/id5-api.js) - Open-source JavaScript library for ID5's universal ID, shipped with a Prebid.js integration module.

![web](image/alg_I.png) [ID5 Submodule Reference](https://docs.prebid.org/dev-docs/modules/userid-submodules/id5.html) - Configuration for the ID5 submodule inside Prebid's User ID module, including proxy options.

![web](image/alg_I.png) [EUID Submodule Reference](https://docs.prebid.org/dev-docs/modules/userid-submodules/euid.html) - Extended user ID configuration for European publishers under the EUID framework.

![web](image/alg_I.png) [Publisher Provided ID Submodule](https://docs.prebid.org/dev-docs/modules/userid-submodules/pubprovided.html) - Passes a publisher's own identifier into the bid stream as an EID.

![web](image/alg_I.png) [LiveIntent Li_ad Submodule](https://docs.prebid.org/dev-docs/modules/userid-submodules/liveintent.html) - Configuration for the LiveIntent identity submodule used alongside email-based addressability.

![github](image/alg_R.png) [Unified ID 2.0 Docs](https://github.com/IABTechLab/uid2docs) - Official UID2 documentation repository covering token generation, operators, SDKs, and Prebid integration.

![github](image/alg_R.png) [UID2 Web Integrations](https://github.com/IABTechLab/uid2-web-integrations) - Reference web integration code for UID2, including the browser SDK and Prebid.js module wiring.

![github](image/alg_R.png) [UID2 Operator](https://github.com/IABTechLab/uid2-operator) - The reference Java implementation of a UID2 operator, covering token minting, matching, and the endpoints clients call.

![github](image/alg_R.png) [UID2 Opt-Out Service](https://github.com/IABTechLab/uid2-optout) - Reference implementation of the opt-out endpoint that UID2 participants operate.

![github](image/alg_R.png) [UID2 Examples](https://github.com/IABTechLab/uid2-examples) - Sample sites demonstrating UID2 and EUID integration patterns, from the JavaScript SDK to server-side token handling.

![github](image/alg_R.png) [UID2 Self-Serve Portal](https://github.com/IABTechLab/uid2-self-serve-portal) - Open-source portal that lets participants administer their own UID2 setup.

![github](image/alg_R.png) [SWAN](https://github.com/SWAN-community/swan) - Open-source, privacy-preserving cross-domain identity network specification and implementation for publishers; dormant since 2021.

![github](image/alg_R.png) [Identity Gatekeeper](https://github.com/prebid/identity-gatekeeper) - Prebid proposals and a working proof of concept for permissioning which identity signals reach which bidders; dormant since 2021.

![github](image/alg_R.png) [UID2 Infrastructure Prototype](https://github.com/prebid/uid2-infrastructure) - Terraform prototype for self-hosting the UID2 operator stack; dormant since 2022.

![web](image/alg_I.png) [ID Import Library Module](https://docs.prebid.org/dev-docs/modules/idLibrary.html) - Collects every identity present on the page and posts them to a configurable endpoint for ID graphing.

![web](image/alg_I.png) [Data Controller Module](https://docs.prebid.org/dev-docs/modules/dataControllerModule.html) - Filters which EIDs and seller-defined audiences each bidder is allowed to receive.

### Consent Signals and Compliance Libraries

![web](image/alg_I.png) [TCF Consent Management Module](https://docs.prebid.org/dev-docs/modules/consentManagementTcf.html) - Reads the TCF string from your CMP, gates adapter calls on purpose enforcement, and passes the signal to bidders.

![web](image/alg_I.png) [GPP Consent Management Module](https://docs.prebid.org/dev-docs/modules/consentManagementGpp.html) - The Global Privacy Platform equivalent, covering US state and regional privacy strings.

![web](image/alg_I.png) [US Privacy Consent Management Module](https://docs.prebid.org/dev-docs/modules/consentManagementUsp.html) - Reads the CCPA/USP string from the CMP and forwards it to adapters.

![web](image/alg_I.png) [CMP Integration Best Practices](https://docs.prebid.org/dev-docs/cmp-best-practices.html) - Community-collected recommendations for wiring Prebid.js to a consent management platform.

![web](image/alg_I.png) [TCF Control Module](https://docs.prebid.org/dev-docs/modules/tcfControl.html) - Enables or suppresses Prebid activities such as device storage and ID syncing based on TCF purposes.

![web](image/alg_I.png) [Storage Control Module](https://docs.prebid.org/dev-docs/modules/storageControl.html) - Audits other modules' use of device storage against their disclosed storage keys and blocks undisclosed access.

![github](image/alg_R.png) [TCF Specification](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework) - IAB Europe's Transparency and Consent Framework technical specs, including the TC string format.

![github](image/alg_R.png) [iabtcf-es](https://github.com/InteractiveAdvertisingBureau/iabtcf-es) - Official TypeScript and JavaScript tool suite for encoding, decoding, and validating TCF v2 consent strings.

![github](image/alg_R.png) [iabtcf-java](https://github.com/InteractiveAdvertisingBureau/iabtcf-java) - Java implementation of the TCF v2 consent string encoding and core libraries.

![github](image/alg_R.png) [Global Privacy Platform](https://github.com/InteractiveAdvertisingBureau/Global-Privacy-Platform) - The GPP specification that consolidates regional privacy signals into a single consent string for the bidstream.

![github](image/alg_R.png) [iabgpp-es](https://github.com/IABTechLab/iabgpp-es) - Official JavaScript library for encoding and decoding GPP consent sections, aimed at CMPs.

![github](image/alg_R.png) [iabgpp-java](https://github.com/IABTechLab/iabgpp-java) - Java implementation of GPP core and section supporting libraries.

![github](image/alg_R.png) [US Privacy Specification](https://github.com/InteractiveAdvertisingBureau/USPrivacy) - Technical specifications for US state privacy signals, starting with the CCPA string.

![github](image/alg_R.png) [go-gdpr](https://github.com/prebid/go-gdpr) - Go implementation of TCF purpose enforcement, the library PBS-Go uses to gate identity and syncing.

![github](image/alg_R.png) [go-gpp](https://github.com/prebid/go-gpp) - Go support for GPP consent sections, the counterpart used for US state regulations.

![github](image/alg_R.png) [Consenti](https://github.com/santoshe61/consenti) - Self-hosted open-source consent platform covering GDPR opt-in, TCF, CCPA, and Global Privacy Control.

![github](image/alg_R.png) [ConsentStack CMP](https://github.com/ConsentStack/cmp) - Open-source, developer-focused consent management platform; dormant since 2018 but still a readable CMP reference implementation.

### Activity Controls and Regional Rules

![web](image/alg_I.png) [Prebid.js Activity Controls](https://docs.prebid.org/dev-docs/activity-controls.html) - The centralized rule set for suppressing storage access, geolocation, and partner data sharing per activity.

![web](image/alg_I.png) [Prebid Server Activity Controls](https://docs.prebid.org/prebid-server/features/pbs-privacy.html) - The server-side equivalent, including the component inventory and default privacy behaviors.

![web](image/alg_I.png) [PBS Activity Control Implementation Guide](https://docs.prebid.org/prebid-server/features/pbs-activitycontrols.html) - How modules and adapters declare and check activities in PBS-Go and PBS-Java.

![web](image/alg_I.png) [How to Add a PBS Privacy Module](https://docs.prebid.org/prebid-server/developers/add-a-privacy-module.html) - How to implement a privacy module or scrubber that plugs into the Prebid Server hook framework.

![web](image/alg_I.png) [GPP US National Control](https://docs.prebid.org/dev-docs/modules/gppControl_usnat.html) - Applies the US national privacy template rules to Prebid activities.

![web](image/alg_I.png) [GPP US State Control](https://docs.prebid.org/dev-docs/modules/gppControl_usstates.html) - Per-state rule sets for sensitive data categories in US privacy regimes.

![web](image/alg_I.png) [DSA Control Module](https://docs.prebid.org/dev-docs/modules/dsaControl.html) - Carries EU Digital Services Act disclosure signals through the auction and into ad-server targeting.

![web](image/alg_I.png) [Multi-State Privacy Act Controls](https://docs.prebid.org/features/mspa-usnat.html) - How US state privacy acts and the US national template map onto Prebid's activity controls.

![web](image/alg_I.png) [Quebec Law 25 Activity Controls](https://docs.prebid.org/features/ac-quebec.html) - How Quebec's privacy regime maps onto Prebid's activity control model.

![web](image/alg_I.png) [Ad Choices Icon Rendering](https://docs.prebid.org/dev-docs/modules/adChoices.html) - Self-rendering the Ad Choices icon when the ad server would otherwise have supplied it.

![web](image/alg_I.png) [Prebid Privacy Resources](https://docs.prebid.org/support/privacy-resources.html) - Prebid.org's index of regulatory guidance, framework docs, and legal-review checklists.

### Cookieless and Edge Addressability

![web](image/alg_I.png) [Topics For First Party Data Module](https://docs.prebid.org/dev-docs/modules/topicsFpdModule.html) - Reads Chrome Topics API segments and injects them into the auction as first-party data.

![web](image/alg_I.png) [Chrome AI RTD Provider](https://docs.prebid.org/dev-docs/modules/chromeAiRtdProvider.html) - Uses Chrome's built-in AI APIs for on-device language detection and summarization to enrich bid requests.

![web](image/alg_I.png) [Prebid PAAPI Module](https://docs.prebid.org/dev-docs/modules/paapi.html) - Collects Protected Audience interest-group bids and merges them into the Prebid auction.

![web](image/alg_I.png) [PAAPI for GPT Module](https://docs.prebid.org/dev-docs/modules/paapiForGpt.html) - Runs the browser-level auction through GPT and passes the auction config to Prebid.

![web](image/alg_I.png) [Chrome Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience-api) - Chrome's on-device auction API: interest groups, key/value service, and the seller and buyer guides.

![github](image/alg_R.png) [1st Party Curated Addressability](https://github.com/IABTechLab/1st-party-curated-addressability) - IAB Tech Lab exploration of publisher-curated audience signals as a substitute for third-party IDs; dormant since 2023.

![github](image/alg_R.png) [PAIR](https://github.com/InteractiveAdvertisingBureau/PAIR) - Publisher Advertiser Identity Reconciliation: matching a user across two parties without either revealing the identifier.

![github](image/alg_R.png) [IAB Tech Lab Privacy Lab](https://github.com/IABTechLab/privacy-lab) - Notebooks and utilities for testing how privacy-enhancing technologies change measurement and attribution outcomes.

---

## Analytics, Monitoring and Performance

*If you cannot reconstruct the auction afterwards, you cannot defend the floor, the timeout, or the bidder mix — and you cannot see what it cost the page.*

### Auction Analytics and Bidstream Logging

![web](image/alg_I.png) [Analytics Adapters for Prebid.js](https://docs.prebid.org/overview/analytics.html) - Index of the vendor analytics adapters that can be compiled into a build and enabled with `pbjs.enableAnalytics()`.

![web](image/alg_I.png) [Generic Analytics Adapter](https://docs.prebid.org/dev-docs/modules/genericAnalyticsAdapter.html) - Publisher-owned adapter that batches any Prebid event to your own endpoint or handler, with sampling and per-event formatters.

![web](image/alg_I.png) [How to Add an Analytics Adapter](https://docs.prebid.org/dev-docs/integrate-with-the-prebid-analytics-api.html) - Architecture and code template for endpoint and bundle adapters hooked into the Prebid event bus.

![web](image/alg_I.png) [pbjs.enableAnalytics() Reference](https://docs.prebid.org/dev-docs/publisher-api-reference/enableAnalytics.html) - Runtime configuration for adapters: event lists, sampling, and per-partner options.

![web](image/alg_I.png) [How to Add a Prebid Server Analytics Adapter](https://docs.prebid.org/prebid-server/developers/pbs-build-an-analytics-adapter.html) - Implementing analytics modules for PBS-Go and PBS-Java, including the filesystem and log examples.

![web](image/alg_I.png) [Instream Video Tracking Module](https://docs.prebid.org/dev-docs/modules/instreamTracking.html) - Lets analytics and bid adapters observe `BID_WON` for instream video bids, which the page otherwise never sees.

![web](image/alg_I.png) [Bid Viewability Module for GAM](https://docs.prebid.org/dev-docs/modules/bidViewable.html) - Fires a `bidViewable` event when a rendered bid meets Active View criteria.

![web](image/alg_I.png) [Generic Viewability Module](https://docs.prebid.org/dev-docs/modules/viewability.html) - Element-level viewability tracking with configurable criteria — note the security disclaimer on the page before using it.

### Performance, Core Web Vitals and Sustainability

![github](image/alg_R.png) [Lighthouse](https://github.com/GoogleChrome/lighthouse) - Google's audit engine for measuring main-thread work, render-blocking scripts, and Core Web Vitals on ad-heavy pages.

![github](image/alg_R.png) [WebPageTest](https://github.com/catchpoint/WebPageTest) - Self-hostable performance testing platform for measuring the ad stack's cost in LCP, INP, and total blocking time.

![github](image/alg_R.png) [web-vitals](https://github.com/GoogleChrome/web-vitals) - The small library for measuring LCP, CLS, INP, TTFB, and FCP from the field, the data most wrapper teams end up charting.

![web](image/alg_I.png) [PageSpeed Insights](https://pagespeed.web.dev/) - Hosted Lighthouse runs with field data, the fastest way to see the cost of an ad-stack change.

![web](image/alg_I.png) [Web Vitals Guide](https://web.dev/vitals/) - Definitions and thresholds for each core metric, including what counts as a good value.

![web](image/alg_I.png) [Publisher Sustainability Best Practices](https://docs.prebid.org/support/sustainability-publishers.html) - Prebid's guidance on build size, bidder count, analytics coverage, and user-sync hygiene.

![web](image/alg_I.png) [Prebid Sustainability Portal](https://docs.prebid.org/support/sustainability-portal.html) - The hub for Prebid.org's carbon-reduction work across publishers, bidders, and analytics.

![web](image/alg_I.png) [Prebid Statement on Sustainability](https://docs.prebid.org/overview/statement-on-sustainability.html) - The technical report behind the program: where the ad stack's emissions actually come from.

### Ad Quality, Fraud and Transparency

![github](image/alg_R.png) [Blacklight](https://github.com/the-markup/blacklight-collector) - Open-source privacy inspector that loads a URL in headless Chrome and reports the ad-tech and tracking scripts it observes.

![github](image/alg_R.png) [Prebid Code Scanner](https://github.com/prebid/code-scanner) - Scans for domains flagged by Prebid member companies; incubating, with the repository as the only documentation.

![web](image/alg_I.png) [Bid Response Filter Module](https://docs.prebid.org/dev-docs/modules/bidResponseFilter.html) - Validates each bid's `ortb2` payload against its `meta` data and drops responses that do not match.

![web](image/alg_I.png) [Confiant RTD Provider](https://docs.prebid.org/dev-docs/modules/confiantRtdProvider.html) - Real-time data provider that blocks security, quality, and privacy threats before the creative renders.

![web](image/alg_I.png) [IAS RTD Provider](https://docs.prebid.org/dev-docs/modules/iasRtdProvider.html) - Injects Integral Ad Science brand suitability signals into the auction so bids can be filtered.

![web](image/alg_I.png) [Brandmetrics RTD Provider](https://docs.prebid.org/dev-docs/modules/brandmetricsRtdProvider.html) - Publisher-side brand safety and viewability rules applied per auction.

![web](image/alg_I.png) [Qortex RTD Provider](https://docs.prebid.org/dev-docs/modules/qortexRtdProvider.html) - Ad quality and safety screening as a real-time data module.

![web](image/alg_I.png) [Mediafilter RTD Provider](https://docs.prebid.org/dev-docs/modules/mediafilterRtdProvider.html) - Filters disallowed advertiser categories and creative attributes out of the bid responses.

---

## Floors, Timeouts and Yield Optimization

*Floors and timeouts move revenue more than most wrapper rewrites — tune them with evidence, not defaults.*

### Price Floors and Currency

![web](image/alg_I.png) [Prebid.js Price Floors Module](https://docs.prebid.org/dev-docs/modules/floors.html) - Schema 2 floor configuration, dynamic floor providers, and enforcement semantics for Prebid.js auctions.

![web](image/alg_I.png) [Prebid Server Price Floors](https://docs.prebid.org/prebid-server/features/pbs-floors.html) - Server-side floor framework that caches floor data and resolves it into `imp.bidfloor` before adapters are called.

![web](image/alg_I.png) [Price Floors Video Overview](https://docs.prebid.org/dev-docs/floors-video-overview.html) - The maintainers walking through floor signaling, enforcement, and dynamic floor providers, with a transcript.

![web](image/alg_I.png) [Currency Module](https://docs.prebid.org/dev-docs/modules/currency.html) - Converts bids into one or more report currencies, with ad-server and bidder overrides.

![github](image/alg_R.png) [Prebid Currency File](https://github.com/prebid/currency-file) - Auto-generated daily FX rates consumed by the Prebid.js currency module and Prebid Server.

![github](image/alg_R.png) [Currency File Generator](https://github.com/prebid/currency-file-generator) - The generator that rebuilds the FX file, so you can see exactly what a rate change means.

![web](image/alg_I.png) [Prebid Server Currency Support](https://docs.prebid.org/prebid-server/features/pbs-currency.html) - How PBS converts floors and bid prices, and which rates file it uses.

### Timeouts, Bidder Count and Auction Shape

![web](image/alg_I.png) [Prebid Timeouts](https://docs.prebid.org/features/timeouts.html) - Explains failsafe, auction, and timeout-adjustment layers, plus how to diagnose adapters that miss the window.

![web](image/alg_I.png) [Video Timeouts and Caching](https://docs.prebid.org/features/timeouts-video.html) - The longer latency budget video needs and how it interacts with caching.

![web](image/alg_I.png) [Timeout RTD Provider](https://docs.prebid.org/dev-docs/modules/timeoutRtdProvider.html) - Sets auction timeouts dynamically from rules or a timeout provider instead of a single static value.

![web](image/alg_I.png) [MultiBid Module](https://docs.prebid.org/dev-docs/modules/multibid.html) - Lets configured bidders pass more than one bid per ad unit to the ad server, raising price competition without more line items.

![web](image/alg_I.png) [Shaping Rules Module](https://docs.prebid.org/dev-docs/modules/shapingRulesModule.html) - Includes or excludes bidders per auction using floors-style conditions on first-party and ad-unit data.

![web](image/alg_I.png) [Previous Auction Info Module](https://docs.prebid.org/dev-docs/modules/previousAuctionInfo.html) - Feeds prior auction results back into the next request so bidders can price against recent history.

![web](image/alg_I.png) [Optimal Header Bidding Setup](https://docs.prebid.org/overview/optimal-header-bidding-setup.html) - Prebid's recommended combination of auction type, caching, and ad-server integration, with the reasoning.

![web](image/alg_I.png) [How Many Bidders for Header Bidding](https://docs.prebid.org/overview/how-many-bidders-for-header-bidding.html) - Evidence on bidder count versus revenue and latency, and where the curve turns.

![web](image/alg_I.png) [Synthetic Inventory Module](https://docs.prebid.org/dev-docs/modules/yieldmoSyntheticInventoryModule.html) - SIM: bids against synthetic slots in long-form content so premium demand can be filled without real placements.

### Real-Time Data and Context Signals

![web](image/alg_I.png) [How to Add a Prebid.js RTD Submodule](https://docs.prebid.org/dev-docs/add-rtd-submodule.html) - The interface for adding data to bid requests or ad-server targeting from a real-time data provider.

![web](image/alg_I.png) [Geolocation RTD Provider](https://docs.prebid.org/dev-docs/modules/geolocationRtdProvider.html) - Requests user location with consent and injects coordinates into the auction.

![web](image/alg_I.png) [Greenbids RTD Provider](https://docs.prebid.org/dev-docs/modules/greenbidsRtdProvider.html) - Filters SSP calls per auction to cut load on the programmatic chain and reduce serving carbon.

![web](image/alg_I.png) [First Party Data Guide](https://docs.prebid.org/features/firstPartyData.html) - The `ortb2` object model, context and user segments, and bidder-level permissions.

![web](image/alg_I.png) [Prebid Server First Party Data](https://docs.prebid.org/prebid-server/features/pbs-fpd.html) - How server-side auctions merge publisher context into the OpenRTB request.

![web](image/alg_I.png) [First Party Data Validation Module](https://docs.prebid.org/dev-docs/modules/validationFpdModule.html) - Warns when your first-party data structure does not match the OpenRTB spec.

![web](image/alg_I.png) [Advanced Size Mapping](https://docs.prebid.org/dev-docs/modules/sizeMappingV2.html) - Media-query driven size and format selection per ad unit, the basis for responsive auction shapes.

### Optimization Guides and Engineering Writing

![web](image/alg_I.png) [Implementing Prebid Server: Q&A](https://clearcode.cc/blog/prebid-server-qa-implementation/) - Architecture interview covering hosted PBS design, auction flow, and the ad-server handoff.

![web](image/alg_I.png) [Header Bidding Archive (Clearcode)](https://clearcode.cc/tag/header-bidding/) - Long-running engineering archive on client-side versus server-side auction design and waterfall dynamics.

![web](image/alg_I.png) [Prebid Blog](https://prebid.org/blog/) - Release notes, project announcements, and engineering posts from the Prebid.org community.

![web](image/alg_I.png) [Prebid.js Release Notes](https://docs.prebid.org/dev-docs/release-notes.html) - Version-by-version breaking changes, including which modules were removed in each major release.

![web](image/alg_I.png) [Prebid.js 11 Notes](https://docs.prebid.org/dev-docs/pb11-notes.html) - The current major release: removed ad pod and category translation modules and their replacements.

---

## Video, CTV and SSAI Tooling

*The long-form and in-stream side of the stack: VAST parsing, players that speak Prebid, and the signalling that stitches ads into a stream.*

### VAST, VMAP and Ad Signal Parsers

![github](image/alg_R.png) [VAST Client JS](https://github.com/dailymotion/vast-client-js) - Dailymotion's VAST parser up to version 6: resolves wrapped tags and returns a structured ad object.

![github](image/alg_R.png) [rmp-vast](https://github.com/radiantmediaplayer/rmp-vast) - Client-side VAST 2, 3, and 4 loader and renderer for HTML5 video, built for ad insertion without a full player SDK.

![github](image/alg_R.png) [vast-parser](https://github.com/unruly/vast-parser) - Recursively fetches and flattens a VAST wrapper chain into a single JavaScript object; dormant since 2022.

![github](image/alg_R.png) [iab-vast-parser](https://github.com/zentrick/iab-vast-parser) - Parses VAST tags into the `iab-vast-model` object graph, shared by Zentrick's players and QA tools; dormant since 2021.

![github](image/alg_R.png) [go-vast](https://github.com/joeig/go-vast) - Go library for parsing, manipulating, and building VAST documents.

![github](image/alg_R.png) [php-vast](https://github.com/sokil/php-vast) - PHP generator and parser for VAST documents, useful in ad-server-side integrations.

![github](image/alg_R.png) [haxqer/vast](https://github.com/haxqer/vast) - Go library implementing VAST 4.3 ad generation and parsing.

![github](image/alg_R.png) [vast-info](https://github.com/Eyevinn/vast-info) - Prints a readable summary of a VAST or VMAP document, the quick check when a tag behaves oddly.

![github](image/alg_R.png) [vastlint](https://github.com/aleksUIX/vastlint) - Rust validator for IAB VAST, VMAP, and DAAST documents with a hosted MCP endpoint at `vastlint.org/mcp`.

![github](image/alg_R.png) [IAB VAST Tester](https://github.com/IABTechLab/VAST-Tester) - Contributed by DoubleVerify to validate VAST ads against the IAB spec; also hosted as a web tool.

![web](image/alg_I.png) [IAB Tech Lab VAST Validator](https://tools.iabtechlab.com/resourcecenter/vastTagValidator) - Hosted validator for VAST tag conformance, no local setup required.

![github](image/alg_R.png) [threefive](https://github.com/superkabuki/threefive_is_scte35) - Python decoder and encoder for SCTE-35, SCTE-104, and SCTE-224 splice information — the signal SSAI decisioning starts from.

![github](image/alg_R.png) [SCTE-35, SCTE-104, SCTE-67 Reference Notes](https://github.com/leandromoreira/scte-35-scte-104-scte-67) - Written explanation of how ad signalling flows from SCTE-104 through SCTE-35 into HLS and DASH cues.

### Players and Prebid Video Integrations

![github](image/alg_R.png) [Open Player JS](https://github.com/openplayerjs/openplayerjs) - HTML5 video and audio player with built-in VAST, VMAP, and IMA3 ad support, commonly paired with Prebid VAST.

![github](image/alg_R.png) [rmp-prebid](https://github.com/radiantmediaplayer/rmp-prebid) - Prebid.js integration for Radiant Media Player, including the adpod helpers for long-form video.

![github](image/alg_R.png) [videojs-vast-vpaid plugin](https://github.com/prebid/videojs-mailonline-plugin) - Prebid.org's fork of the MailOnline Video.js plugin that renders VAST and VPAID ads inside a Video.js player; dormant since 2021.

![github](image/alg_R.png) [videojs-mediatailor-ssai](https://github.com/dds05/videojs-mediatailor-ssai) - Video.js plugin that plays an AWS MediaTailor server-side ad insertion manifest in a standard web player.

![web](image/alg_I.png) [Prebid Server Video Adapter Overview](https://docs.prebid.org/dev-docs/pbsBidAdapter-video-overview.html) - How VAST requests differ between client-side and server-side video auctions.

![web](image/alg_I.png) [How to Add a Video Submodule](https://docs.prebid.org/dev-docs/add-video-submodule.html) - Contract for supporting a new player inside Prebid's video module.

![web](image/alg_I.png) [Prebid Mobile Video Flow](https://docs.prebid.org/prebid-mobile/prebid-mobile-video-flow.html) - The sequence a rewarded or interstitial video request follows through the SDK and PBS.

![web](image/alg_I.png) [Prebid Identity for Video and CTV](https://docs.prebid.org/identity/prebid-identity-video.html) - How identifiers are passed in long-form and CTV auctions where cookies are not an option.

![web](image/alg_I.png) [Setting Up Prebid Video in GAM](https://docs.prebid.org/adops/setting-up-prebid-video-in-dfp.html) - Trafficking VAST line items and the universal creative for video auctions.

![web](image/alg_I.png) [Setting Up Prebid Video in Freewheel](https://docs.prebid.org/adops/setting-up-prebid-video-in-freewheel.html) - The same setup for a video ad server instead of a display one.

---

## Open Ad Servers, DSPs and Reference Implementations

*Working code for the other side of the auction. Read these to understand what a wrapper is actually negotiating with.*

### Ad Servers and Supply Platforms

![github](image/alg_R.png) [Revive Adserver](https://github.com/revive-adserver/revive-adserver) - The long-standing open-source ad serving system: campaigns, targeting, banners, zones, and third-party ad tags.

![github](image/alg_R.png) [Ethical Ad Server](https://github.com/readthedocs/ethical-ad-server) - Read the Docs' ad server for privacy-respecting campaigns: no cross-site tracking, with reporting built for publishers and advertisers.

![github](image/alg_R.png) [openadserver](https://github.com/seanZhang414/openadserver) - Self-hosted ad serving platform that pairs campaign delivery with ML-based CTR prediction; a young project, read the README before depending on it.

### Bidding Engines and Protocol Libraries

![github](image/alg_R.png) [vanilla-rtb](https://github.com/venediktov/vanilla-rtb) - Modular C++ framework for building a demand-side platform, covering request log parsing, bidding, and model training.

![github](image/alg_R.png) [rapid-bidder](https://github.com/vanilla-rtb/rapid-bidder) - Production DSP built on the vanilla-rtb stack, kept as the worked example of the framework; dormant since 2017.

![github](image/alg_R.png) [vanilla-rtb extensions](https://github.com/vanilla-rtb/extensions) - Code generators and extensions for the vanilla-rtb stack, including OpenRTB model generation.

![github](image/alg_R.png) [bool-expr-indexer](https://github.com/csimplestring/bool-expr-indexer) - Boolean expression index used for RTB ad selection, the targeting-matching problem in its raw form.

![github](image/alg_R.png) [OpenRTB Go Types](https://github.com/prebid/openrtb) - Maintained Go types and enums for OpenRTB 2.x, 3.0, AdCOM, and Native, used by Prebid Server.

![github](image/alg_R.png) [bsm/openrtb](https://github.com/bsm/openrtb) - Widely copied Go OpenRTB definitions; archived in 2024, so use it to read older Go bidders.

![github](image/alg_R.png) [mxmCherry/openrtb](https://github.com/mxmCherry/openrtb) - The fork that added OpenRTB 3.0 and AdCOM types, also archived; still a reference for older codebases.

![github](image/alg_R.png) [openrtb-typescript](https://github.com/ClearcodeHQ/openrtb) - Clearcode's TypeScript types for OpenRTB 2.5 and 3.0 with request and response validation.

![github](image/alg_R.png) [iab-types](https://github.com/hogekai/iab-types) - TypeScript type definitions for IAB Tech Lab's AdCOM, OpenRTB, and Native specs, kept in sync with the specifications.

![github](image/alg_R.png) [openrtb-proto-v2](https://github.com/IABTechLab/openrtb-proto-v2) - IAB Tech Lab's protobuf model for OpenRTB 2.x, the source of generated clients across languages.

![github](image/alg_R.png) [adcom-proto](https://github.com/IABTechLab/adcom-proto) - Protobuf definitions for AdCOM, the domain layer beneath OpenRTB 2.6 and 3.0.

![github](image/alg_R.png) [openrtb3-converter](https://github.com/InteractiveAdvertisingBureau/openrtb3-converter) - Converts OpenRTB 2.5 and 2.6 payloads to and from the 3.0 layer structure for migration testing.

![github](image/alg_R.png) [iab-rust](https://github.com/klaussilveira/iab-rust) - Idiomatic Rust data structures for OpenRTB, AdCOM, and related IAB specifications.

![github](image/alg_R.png) [rtblint](https://github.com/aleksUIX/rtblint) - OpenRTB linter that validates 2.x bid requests and responses against versioned schemas and spec rules.

### Tutorials and Reference Architectures

![github](image/alg_R.png) [adserver-tutorial](https://github.com/kijepark/adserver-tutorial) - Node.js ad server built step by step, from request handling through targeting to the auction.

![github](image/alg_R.png) [prebid.github.io](https://github.com/prebid/prebid.github.io) - The source of every page on docs.prebid.org — the place to fix a doc you found wrong.

---

## Specifications and Standards

*Primary sources only — every field in a bid request traces back to one of these documents.*

### Auction Protocols

![github](image/alg_R.png) [OpenRTB 2.x Specification](https://github.com/InteractiveAdvertisingBureau/openrtb2.x) - The current 2.6+ spec, its community extension framework, and protobuf definitions.

![github](image/alg_R.png) [OpenRTB 3.0 Specification](https://github.com/InteractiveAdvertisingBureau/openrtb) - The layered 3.0 transaction model built on AdCOM, with request and response object definitions.

![github](image/alg_R.png) [AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM) - The Advertising Common Object Model that supplies the domain layer and enum lists for OpenRTB 2.6 and 3.0.

![github](image/alg_R.png) [OpenRTB Data Models](https://github.com/InteractiveAdvertisingBureau/openrtb-model) - Machine-readable data models for OpenRTB 2.x and 3.0, useful for code generation and validation.

![github](image/alg_R.png) [IAB Tech Lab Taxonomies](https://github.com/InteractiveAdvertisingBureau/Taxonomies) - Machine-readable content, audience, and ad-product taxonomies with IDs, used for `cattax` and `segtax` fields.

![github](image/alg_R.png) [iab-mapper](https://github.com/IABTechLab/iab-mapper) - Local tool that maps content categories between IAB Taxonomy 2.x and 3.0, deterministic with optional fuzzy matching.

![github](image/alg_R.png) [iab-taxonomy-classifier](https://github.com/IABTechLab/iab-taxonomy-classifier) - Toolkit for classifying content into the IAB Tech Lab Content Taxonomy with embedding models, plus an evaluation harness for comparing them.

![github](image/alg_R.png) [Native Ads Specification](https://github.com/InteractiveAdvertisingBureau/Native-Ads) - The native ad object model and asset types that let a publisher render a bid in its own layout.

![github](image/alg_R.png) [Flexible Ad Testing Samples](https://github.com/InteractiveAdvertisingBureau/flex-ad-testing) - Helper code and samples for exercising the IAB flexible ad format specifications.

![github](image/alg_R.png) [Category Mapping File](https://github.com/prebid/category-mapping-file) - Default IAB sub-category to ad-server category translation files used for long-form video, served from a CDN.

### Supply Path, Authorization and Transparency

![web](image/alg_I.png) [ads.txt Specification](https://iabtechlab.com/ads-txt/) - The authoritative ads.txt and app-ads.txt specification for declaring authorized sellers of inventory.

![web](image/alg_I.png) [sellers.json and SupplyChain](https://iabtechlab.com/sellers-json/) - Specifications and implementation guidance for verifying who sells an impression and how it traveled through the chain.

![github](image/alg_R.png) [ads.txt Crawler](https://github.com/InteractiveAdvertisingBureau/adstxtcrawler) - Reference Python crawler that fetches and parses ads.txt files at scale.

![github](image/alg_R.png) [ads.txt Parser (Go)](https://github.com/InteractiveAdvertisingBureau/ads.txt-parser) - IAB Tech Lab's reference Go parser, currently focused on app-ads.txt.

![github](image/alg_R.png) [ads.txt](https://github.com/perry-mitchell/ads.txt) - JavaScript parser and generator for ads.txt files, usable on both sides of the relationship.

![github](image/alg_R.png) [go-adstxt](https://github.com/suzuken/go-adstxt) - Go parser for ads.txt used in bulk validation jobs.

![github](image/alg_R.png) [adscrawler](https://github.com/appgoblin-dev/adscrawler) - Crawler that resolves app store listings, SDK identifiers, and app-ads.txt entries to reconcile mobile sellers.

![web](image/alg_I.png) [SupplyChain Object (schain) Module](https://docs.prebid.org/dev-docs/modules/schain.html) - How Prebid builds and forwards the OpenRTB supply chain object for display and video requests.

![web](image/alg_I.png) [DealChain Object (dchain) Module](https://docs.prebid.org/dev-docs/modules/dchain.html) - The deal-path equivalent, recording intermediaries for a programmatic guaranteed transaction.

![web](image/alg_I.png) [ads.cert Program](https://iabtechlab.com/ads-cert) - The suite of protocols for authenticated connections and verified creatives, with current status of each part.

![github](image/alg_R.png) [adscert](https://github.com/IABTechLab/adscert) - Go implementation of the ads.cert Authenticated Connections Protocol for signing buyer requests.

![github](image/alg_R.png) [ads.cert OpenRTB 3 Verifier](https://github.com/InteractiveAdvertisingBureau/ads-cert-openrtb3-verifier) - Java verifier for checking RSA signatures on OpenRTB 3.0 requests; dormant since 2019.

![web](image/alg_I.png) [Curated Audiences (SDA) Specification](https://iabtechlab.com/sda/) - The seller-defined audiences framework, renamed Curated Audiences, for passing publisher-owned segments in OpenRTB.

![web](image/alg_I.png) [Addressability and PETs Standards](https://iabtechlab.com/standards/addressability-and-pets/) - IAB Tech Lab's index of addressability and privacy-enhancing-technology standards, with the release status of each.

### Video, Creative and Measurement Standards

![github](image/alg_R.png) [VAST Specification](https://github.com/InteractiveAdvertisingBureau/VAST) - The Video Ad Serving Template spec that defines how a video ad is described, wrapped, and tracked.

![github](image/alg_R.png) [VAST Samples](https://github.com/InteractiveAdvertisingBureau/VAST_Samples) - Sample VAST tags covering the major use cases, the fixtures most parser test suites are built from.

![github](image/alg_R.png) [VMAP Specification](https://github.com/InteractiveAdvertisingBureau/vmap) - Video Multiple Ad Playlist: how ad breaks are declared along a content timeline.

![github](image/alg_R.png) [DAAST Specification](https://github.com/InteractiveAdvertisingBureau/daast) - The Digital Audio Ad Serving Template for podcast and streaming audio inventory.

![github](image/alg_R.png) [SIMID Specification](https://github.com/InteractiveAdvertisingBureau/SIMID) - Secure Interactive Media Interface Definition: the messaging channel between a player and an interactive creative.

![github](image/alg_R.png) [VPAID Specification](https://github.com/InteractiveAdvertisingBureau/vpaid) - The legacy Video Player-Ad Interface Definition, kept here because older creatives still ship it; superseded by SIMID.

![github](image/alg_R.png) [OpenVV](https://github.com/InteractiveAdvertisingBureau/openvv) - The original open video viewability measurement approach and its reference implementation; dormant since 2018.

![github](image/alg_R.png) [OpenVV HTML5](https://github.com/InteractiveAdvertisingBureau/openvv-html) - Viewability measurement for HTML5 video players using time and pixel geometry signals.

![github](image/alg_R.png) [Open Measurement JS Clients](https://github.com/InteractiveAdvertisingBureau/Open-Measurement-JSClients) - IAB Tech Lab's OMID JavaScript SDK for verification vendors and apps, the successor to vendor-specific measurement tags.

![github](image/alg_R.png) [Digital Video Ad Format Guidelines for CTV](https://github.com/InteractiveAdvertisingBureau/Ad-Format-Guidelines-for-Digital-Video-CTV) - Technical requirements for CTV ad units, including interactive and audio-only constraints.

![github](image/alg_R.png) [Live Event Ad Playbook](https://github.com/IABTechLab/Live-Event-Ad-Playbook) - Implementation guidance for monetizing live events with digital video ads and interactive overlays.

![github](image/alg_R.png) [Podcast Technical Measurement Spec](https://github.com/IABTechLab/Podcast-Technical-Measurement) - Technical measurement standards for publisher-hosted podcast ad delivery.

![github](image/alg_R.png) [Brand Suitability Test Benchmarks](https://github.com/IABTechLab/Brand-Suitability-Test-Benchmarks) - Human-labeled media content used to benchmark brand suitability models against the GARM standard.

![github](image/alg_R.png) [OpenDirect Specification](https://github.com/InteractiveAdvertisingBureau/OpenDirect) - The protocol for programmatic direct deals: RFP, IO, and creative exchange in machine-readable form.

![github](image/alg_R.png) [Deals API](https://github.com/IABTechLab/deal-api) - IAB Tech Lab's API specification for negotiating and executing programmatic guaranteed deals.

### Agentic and AI-Era Protocols

![github](image/alg_R.png) [AdCP](https://github.com/adcontextprotocol/adcp) - Ad Context Protocol: an open standard that lets AI agents discover inventory, buy media, and activate packages, with MCP and A2A transports.

![web](image/alg_I.png) [AdCP Documentation](https://docs.adcontextprotocol.org) - Protocol specification, integration guides, and the task reference for AdCP implementations.

![github](image/alg_R.png) [Prebid Sales Agent](https://github.com/prebid/salesagent) - Prebid.org's open-source implementation of the AdCP seller agent role, letting agents discover and buy inventory; alpha.

![github](image/alg_R.png) [AAMP](https://github.com/IABTechLab/AAMP) - Umbrella repository for IAB Tech Lab's Agentic Advertising Management Protocols, indexing each protocol in the family.

![github](image/alg_R.png) [Agentic Real Time Framework](https://github.com/IABTechLab/agentic-real-time-framework) - ARTF: the OpenRTB-derived object model for agent-driven real time bidding, with generated protobuf schemas.

![web](image/alg_I.png) [Agentic Real Time Framework Site](https://iabtechlab.com/standards/artf/) - The public specification page for ARTF and its working group status.

![github](image/alg_R.png) [Buyer Agent](https://github.com/IABTechLab/buyer-agent) - IAB Tech Lab's reference AI media-buying agent built on OpenDirect 2.1, for DSPs and agencies.

![github](image/alg_R.png) [Seller Agent](https://github.com/IABTechLab/seller-agent) - The publisher and SSP counterpart: deal negotiation, booking, and distribution over OpenDirect, Deals API, and sellers.json.

![github](image/alg_R.png) [OpenProposal](https://github.com/IABTechLab/OpenProposal) - The AAMP 3.0 object model describing what is bought and sold so a buying agent can evaluate it at machine speed.

![github](image/alg_R.png) [AgenticDirect](https://github.com/IABTechLab/agentic-direct) - Schema-driven A2A and MCP implementation of OpenDirect 2.1 for direct-deal automation.

![github](image/alg_R.png) [Agentic Audiences](https://github.com/IABTechLab/agentic-audiences) - The open standard, formerly User Context Protocol, for how intelligent agents exchange user context signals.

![github](image/alg_R.png) [Agentic Mobile](https://github.com/IABTechLab/agentic-mobile) - Standard interfaces for agents to discover, configure, and optimize mobile in-app advertising supply and demand.

![github](image/alg_R.png) [Content Monetization Protocols](https://github.com/IABTechLab/CoMP) - IAB Tech Lab's CoMP initiative; see the linked Tech Lab page for current scope and status.

![github](image/alg_R.png) [supply-ops-agent](https://github.com/mpessis/supply-ops-agent) - MCP server exposing sell-side diagnostics — bid rate analysis, IVT checks, ads.txt compliance — built on AAMP standards.

![github](image/alg_R.png) [advertising-hub](https://github.com/itallstartedwithaidea/advertising-hub) - Curated open-source collection of advertising platform APIs, MCP servers, and agent integrations.

![web](image/alg_I.png) [Model Context Protocol](https://modelcontextprotocol.io/) - The transport most ad-tech agent integrations, including AdCP and the GAM and VAST MCP servers, are built on.

---

## Documentation, Learning and Community

*Where wrapper regressions get reported first, and where the reasoning behind the specs is argued out.*

### Prebid Documentation and Orientation

![web](image/alg_I.png) [Prebid Documentation Home](https://docs.prebid.org/) - The reference for Prebid.js, Prebid Server, and Prebid Mobile, with per-release versioning.

![web](image/alg_I.png) [Intro to Header Bidding](https://docs.prebid.org/overview/intro-to-header-bidding.html) - The official explainer of the auction model, wrapper responsibilities, and terminology.

![web](image/alg_I.png) [Header Bidding Glossary](https://docs.prebid.org/overview/glossary.html) - Definitions for media types, formats, and auction terms as Prebid uses them.

![web](image/alg_I.png) [Intro to Header Bidding Video](https://docs.prebid.org/overview/intro-to-header-bidding-video.html) - The same material as a recorded walkthrough, with the auction diagram built step by step.

![web](image/alg_I.png) [Ad Ops Overview Video](https://docs.prebid.org/adops/adops-overview-video.html) - The trafficking and line-item side, aimed at operators rather than developers.

![web](image/alg_I.png) [All Prebid Videos](https://docs.prebid.org/overview/all-videos.html) - Index of the community's recorded talks, module walkthroughs, and conference sessions.

![web](image/alg_I.png) [What is Prebid.org?](https://docs.prebid.org/overview/what-is-prebid-org.html) - Governance, membership, and how decisions about the spec and the code get made.

![web](image/alg_I.png) [Prebid Management Committees](https://docs.prebid.org/overview/prebid-management-committees.html) - Which committee owns adapters, identity, mobile, and analytics — useful before opening a proposal.

![web](image/alg_I.png) [Prebid Principles](https://prebid.org/principles.html) - The project's stated commitments: open, publisher-controlled, and vendor-neutral.

![web](image/alg_I.png) [Wrapper Code of Conduct](https://prebid.org/wrapper_code_of_conduct.html) - The rules that govern fair treatment of demand partners inside a wrapper.

![web](image/alg_I.png) [Prebid Support](https://docs.prebid.org/support/) - Official support routes, including the Ad Ops Slack `#HeaderBidding` channel, GitHub issues, and contact forms.

### Blogs, Newsletters and Industry Press

![web](image/alg_I.png) [AdExchanger](https://www.adexchanger.com/) - Programmatic industry reporting on auctions, identity, and supply-path economics.

![web](image/alg_I.png) [AdMonsters](https://www.admonsters.com/) - Ad ops community and newsletter covering GAM, yield management, and wrapper operations.

![web](image/alg_I.png) [Digiday](https://digiday.com/) - Publisher-side advertising business coverage, including programmatic and CTV economics.

![web](image/alg_I.png) [Streaming Media](https://www.streamingmedia.com/) - Video and CTV engineering coverage: SSAI, ad insertion, and player integration.

![web](image/alg_I.png) [Google Ads Developer Blog](https://ads-developers.googleblog.com/) - Google's developer blog covering Ad Manager API, GPT, and Ads API changes.

### Communities and Q&A

![web](image/alg_I.png) [Ad Ops Slack, #HeaderBidding](https://redditadops.slack.com/messages/C0HVALS8P/) - The channel Prebid.org points publishers to for operational questions and release chatter.

![github](image/alg_R.png) [Prebid.js GitHub Issues](https://github.com/prebid/Prebid.js/issues) - Where adapter regressions and module bugs get filed before they appear anywhere else.

![web](image/alg_I.png) [r/adops](https://www.reddit.com/r/adops/) - Practitioner subreddit for floors, GAM line items, waterfall debugging, and SSP comparisons.

![web](image/alg_I.png) [Stack Overflow: prebid.js](https://stackoverflow.com/questions/tagged/prebid.js) - Tagged Q&A for concrete implementation errors in Prebid.js integrations.

![web](image/alg_I.png) [Stack Overflow: google-ad-manager](https://stackoverflow.com/questions/tagged/google-ad-manager) - Tagged Q&A for GPT, line items, and Ad Manager API questions.

![web](image/alg_I.png) [Prebid Contact Form](https://prebid.org/contact-us/) - The route to the project for issues that do not belong in a public issue tracker.

### Related Awesome Lists

![github](image/alg_R.png) [awesome-rtb](https://github.com/vanilla-rtb/awesome-rtb) - Curated list of real time bidding frameworks, libraries, and datasets, strongest on the demand side.

![github](image/alg_R.png) [awesome-ads](https://github.com/cenoura/awesome-ads) - Broad list of advertising resources, libraries, and specs, with a healthy set of Prebid and OpenRTB links.

![github](image/alg_R.png) [awesome-adtech](https://github.com/AirGrid/awesome-adtech) - Community-curated index of ad tech companies, protocols, and open-source projects; last updated 2021.

![github](image/alg_R.png) [awesome-agentic-advertising](https://github.com/jshorwitz/awesome-agentic-advertising) - Curated list of MCP servers, protocols, and tools for AI-driven advertising work.

![github](image/alg_R.png) [awesome-adops-site](https://github.com/adops-tool/awesome-adops-site) - Companion list of AdOps and ad tech resources, including tooling that sits around the auction.

![github](image/alg_R.png) [awesome-programmatic](https://github.com/adops-tool/awesome-programmatic) - Sibling list covering programmatic platforms, ad servers, and DSP and SSP frameworks.

---

## Contributing

**Contributing to Awesome Header Bidding**

First off, thank you for considering contributing to Awesome Header Bidding. We appreciate your time and effort in helping us keep the definitive index of the open-source programmatic stack accurate.

The goal of this project is to curate a high-quality list of header bidding engines, debuggers, identity and consent modules, floor tooling, and the specifications behind them. To maintain the quality of this list, please review the guidelines below before submitting a pull request.

By participating in this project you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

**Submission Guidelines**

Please ensure your submission adheres to the following core criteria:

- **Relevance:** The resource must sit inside the auction path — a wrapper, an auction server, a module, a debugging tool, a specification, or the reference code around them. Vendor features that are not open source belong in the tool's own docs, not here.
- **Active Maintenance:** We only accept active projects or resources that still explain a working architecture. Abandoned code is accepted only when it remains a useful reference, and must be labeled with the year it stopped.
- **Direct Links Only:** Absolutely no affiliate, tracking, or referral links are allowed. Link to the repository or the resource itself, never to a search engine or a redirect service.

**Description Standards**

Descriptions must be concise, objective, and purely informational.

- **Do:** Focus on the exact utility and where the resource sits in the auction.
  > *Example: "Generates Google Ad Manager line items and key-value targeting from a Prebid.js configuration file."*
- **Don't:** Use marketing fluff, superlatives, or subjective claims.
  > *Example: "The world's best header bidding platform that revolutionizes yield."*
- **Don't:** Include pricing, tiers, or promotional claims in the description.

**Step-by-Step Submission Process**

To add a resource to the list, please follow these steps:

1. **Star the repository:** Show your support and help the community grow.
2. **Locate the file:** Navigate to the `README.md` file in the main branch of this repository.
3. **Edit the document:** Click the "Edit" (pencil) icon to begin making your changes.
4. **Format your entry:** Add your link to the appropriate category using the exact Markdown syntax below. Use the `github` icon when the primary link is a GitHub repository and the `web` icon otherwise. Always link directly to the tool's site or repository — never through search engines or redirect services:

```markdown
![github](image/alg_R.png) [Tool Name](https://github.com/org/repo) - Short, objective description of what it does.

![web](image/alg_I.png) [Tool Name](https://example.com) - Short, objective description of what it does.
```

5. **Run the checks locally:** See **Automated checks** below.
6. **Create a Pull Request:** Submit your PR with a clear and descriptive title using the following format: `Add [Tool Name]`.

**Automated checks**

The repository has one check, a Markdown validator that every pull request must pass:

```bash
python3 scripts/validate_readme.py
```

It verifies that every entry uses a known icon and the documented format, that no URL is listed twice, that every category in the Table of Contents has a matching heading (and vice versa), that local image and file paths resolve, and that links are `https`. Fix any reported line before opening a pull request — the CI workflow runs the same script.

---

## License

Released under [CC0 1.0 Universal](LICENSE) — the list is dedicated to the public domain, so copy, remix, and redistribute it without attribution.

Prebid, OpenRTB, ads.txt, sellers.json, and related names are the property of their respective owners; links are provided for identification only.

[![CC0](https://img.shields.io/badge/CC0-1.0-lightgrey?style=flat-square)](LICENSE)
