## [3.4.0-rc.2](https://github.com/charbonnierg/kapla-cli/compare/v3.4.0-rc.1...v3.4.0-rc.2) (2021-08-28)


### Features

* bumped dependencies and support python3.7 ([cb010a6](https://github.com/charbonnierg/kapla-cli/commit/cb010a695487799603dc756bfb151378ede0b60c))

## [3.4.0-rc.1](https://github.com/charbonnierg/kapla-cli/compare/v3.3.0...v3.4.0-rc.1) (2021-08-28)


### Features

* bumped dependencies ([07e08a6](https://github.com/charbonnierg/kapla-cli/commit/07e08a64fe208b92bb5037f20a7ed87b3841fe62))

## [3.3.0](https://github.com/charbonnierg/kapla-cli/compare/v3.2.0...v3.3.0) (2021-06-15)


### Features

* added list command ([98d3b32](https://github.com/charbonnierg/kapla-cli/commit/98d3b32c55de6b65e2dc1dedb6a27f08bedb5e99))


### Bug Fixes

* create new apps, libraries and plugins handle prefix usage ([535b40a](https://github.com/charbonnierg/kapla-cli/commit/535b40a0b43080693b338341a6a77c85c9bda6d2))
* fix k install which was broken in last commit ([25e906c](https://github.com/charbonnierg/kapla-cli/commit/25e906ce9de0e75c7c25eba91d2db3815e9e28cd))

## [3.3.0-rc.3](https://github.com/charbonnierg/kapla-cli/compare/v3.3.0-rc.2...v3.3.0-rc.3) (2021-06-15)


### Bug Fixes

* fix k install which was broken in last commit ([fde2dd3](https://github.com/charbonnierg/kapla-cli/commit/fde2dd3e73bc74505d2a46b9709b223b3b7c6b67))

## [3.3.0-rc.2](https://github.com/charbonnierg/kapla-cli/compare/v3.3.0-rc.1...v3.3.0-rc.2) (2021-06-15)


### Bug Fixes

* create new apps, libraries and plugins handle prefix usage ([3564a2e](https://github.com/charbonnierg/kapla-cli/commit/3564a2e46a40fef1123fd494b96842a6f26c685b))

## [3.3.0-rc.1](https://github.com/charbonnierg/kapla-cli/compare/v3.2.0...v3.3.0-rc.1) (2021-06-15)


### Features

* added list command ([33e666a](https://github.com/charbonnierg/kapla-cli/commit/33e666a1298ff62587e40da46e05ccd7bbd7dd0b))

## [3.2.0](https://github.com/charbonnierg/kapla-cli/compare/v3.1.0...v3.2.0) (2021-06-15)


### Features

* added k dep command to install same dependency in several projects quickly ([1368b7e](https://github.com/charbonnierg/kapla-cli/commit/1368b7e87a9ee23f305eeddd762e63f627232d2a))


### Bug Fixes

* bumped dependencies ([089e131](https://github.com/charbonnierg/kapla-cli/commit/089e1311cf5fb4fff863cba1158e8cdbe490b53c))
* fix typechecking errors using type: ignore statements ([8723edb](https://github.com/charbonnierg/kapla-cli/commit/8723edb3f04468bf9c4019ad1f1011f17efdfbc7))


## [3.1.0](https://github.com/charbonnierg/kapla-cli/compare/v3.0.4...v3.1.0) (2021-04-21)


### Features

* **cli:** refactored cli and introduced k profile commands ([427d7ae](https://github.com/charbonnierg/kapla-cli/commit/427d7aec9f59238fbe1b4b3406ad4f84235bc60b))

## [3.1.0-rc.1](https://github.com/charbonnierg/kapla-cli/compare/v3.0.4...v3.1.0-rc.1) (2021-04-21)


### Features

* **cli:** refactored cli and introduced k profile commands ([427d7ae](https://github.com/charbonnierg/kapla-cli/commit/427d7aec9f59238fbe1b4b3406ad4f84235bc60b))

### [3.0.4](https://github.com/charbonnierg/kapla-cli/compare/v3.0.3...v3.0.4) (2021-04-20)


### Bug Fixes

* support long format dependencies when bumping versions ([4fc56d2](https://github.com/charbonnierg/kapla-cli/commit/4fc56d2974afac00b7309baf2885980fc3bae258))

## [3.0.3](https://github.com/charbonnierg/kapla-cli/compare/v3.0.2...v3.0.3) (2021-04-20)

### Bug Fixes

- indicate correct version when bumping ([821568c](https://github.com/charbonnierg/kapla-cli/commit/821568c79a4c4faa652aef49dd3fc7dfcbefe350))

## [3.0.2](https://github.com/charbonnierg/kapla-cli/compare/v3.0.1...v3.0.2) (2021-04-20)

### Bug Fixes

- support spaces and dashes in project name, ignore env in glob expr ([26780ca](https://github.com/charbonnierg/kapla-cli/commit/26780caad2ed82765576410cbb39324d990ea5f3))

## [3.0.1](https://github.com/charbonnierg/kapla-cli/compare/v3.0.0...v3.0.1) (2021-04-19)

### Bug Fixes

- **cli:** support path with spaces ([b5baf8a](https://github.com/charbonnierg/kapla-cli/commit/b5baf8ad27c7c4b4ffa6db245a26eb8fa1ca4f4d))

## 1.0.0 (2021-04-12)

### Features

- **cli:** introduced builder subcommand that can be used to manage docker images with builder.yml files ([7b021c0](https://github.com/charbonnierg/kapla-cli/commit/7b021c0c4a64d00e9803c7cd7da270d18dcb84b4))

### Bug Fixes

- **cli:** fix --tags parsing in builder build command ([2f6c7fa](https://github.com/charbonnierg/kapla-cli/commit/2f6c7fa82476b6100eedf2bf2f41e0147dfcd83a))

## 1.0.0-rc.1 (2021-04-11)

### Features

- **cli:** separate cli commands dedicated to generating projects from others ([fd85556](https://github.com/charbonnierg/kapla-cli/commit/fd855560e811f0b374632d643ac0ddcf7d09d05a))
