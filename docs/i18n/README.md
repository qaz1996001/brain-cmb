# brain-cmb

## Overview

**brain-cmb** is a Python package for cerebral microbleed (CMB) detection and analysis in neuroimaging, with integrated DICOM-SEG support for clinical workflows.

## Key Features

- **CMB Detection Pipeline**: Automated detection of cerebral microbleeds from brain MRI scans
- **DICOM-SEG Integration**: Export segmentation results in standardized DICOM-SEG format
- **PipelineCore Architecture**: Built on modular pipeline framework for extensibility
- **Clinical Workflow Support**: Direct integration with medical imaging systems

## Installation

### Requirements

- Python >= 3.10
- Dependencies managed via `uv` package manager

### Install from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/brain-cmb.git
cd brain-cmb

# Install dependencies with uv
uv sync

# Install the package
uv pip install -e .
```

## Quick Start

### Basic Usage

```python
from brain_cmb import main

# Run CMB detection pipeline
main()
```

### Command Line Interface

```bash
# Execute brain-cmb pipeline
brain-cmb
```

## Project Structure

```
brain-cmb/
├── src/
│   └── brain_cmb/
│       ├── core/           # Core CMB detection logic
│       ├── dicomseg/       # DICOM-SEG export functionality
│       │   ├── builder.py  # DICOM-SEG builder
│       │   └── schema/     # CMB segmentation schemas
│       └── pipeline_cmb_tensorflow.py  # TensorFlow-based pipeline
├── docs/                   # Documentation
│   ├── i18n/              # Internationalization docs
│   ├── workflows/         # Development workflows
│   └── releases/          # Release management
├── tests/                  # Test suite
└── pyproject.toml         # Project configuration
```

## Dependencies

Core dependencies include:
- `pipelinecore`: Modular pipeline framework
- `pydicom-seg`: DICOM-SEG format support
- `nibabel`: Neuroimaging data I/O
- `tensorflow`: Deep learning framework
- `pandas`, `matplotlib`, `tqdm`: Data processing and visualization

## Documentation

- [中文文檔](./README.zh-TW.md) - Traditional Chinese documentation
- [Development Workflows](../workflows/) - Git and GitHub workflows
- [Release Management](../releases/) - Version control and release process

## Development

### Setting Up Development Environment

```bash
# Install development dependencies
uv sync --dev

# Run tests
pytest tests/

# Run linting
ruff check src/
```

### Git Workflow

This project follows a feature branch workflow. See [Git Workflow Guide](../workflows/git-workflow.md) for detailed instructions.

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes following conventional commits
4. Push to your fork and create a Pull Request
5. Ensure CI/CD checks pass

## Version History

Current version: **0.1.0**

See [CHANGELOG.md](../../CHANGELOG.md) for detailed version history.

## License

[Specify your license here]

## Contact

- Author: user
- Email: a03440@tmu.edu.tw

## Acknowledgments

Built with [PipelineCore](https://github.com/yourusername/pipelinecore) framework.

---

**Languages**: [English](./README.md) | [繁體中文](./README.zh-TW.md)
