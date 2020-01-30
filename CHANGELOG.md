# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Notes on increasing the i2c baudrate.
- `__pycache__` to `.gitignore`

### Changed
- Changed `time-lapse.py` so it runs faster (i2c baudrate increased on Pi), has currently commented out lines
  for limiting how many images it captures and moved some lines of code around to try and boost performance.
  
### Fixed
- Added exception catch to `thermal-to-images.py` for a `ValueError`. Caused by `Nan` conversion to float.

## [1.0.1] - 2020-01-29
### Added
- Blank line at the end of `requirements.txt` for clarity.

### Fixed
- `camera.py` was loading removed images, this was no longer needed.
- `camera.py` was calling the wrong method.
- `thermal.py` was not calling the class method.

## [1.0.0] - 2020-01-28
### Added
- Initial version.
- `README.md` has details on the repo.
