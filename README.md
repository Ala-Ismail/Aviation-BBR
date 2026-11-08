# Aviation BBR

FPGA/VHDL development for an aviation flight instrument data recorder, covering continuous acquisition, buffering, persistent storage, integrity checks, and data readback.

## Project status

The repository currently contains a requirements study and proposed design direction. RTL, testbenches, build scripts, and hardware validation are not yet included.

The planning baseline in the design study uses an Intel MAX 10 `10M50DAF484I7G`, mirrored F-RAM staging, and a raw NAND archive. These are proposed design choices; see the study for assumptions and open decisions. This repository does not establish aviation certification or approval for installation.

## Documentation

- [Aviation BBR design study](Aviation_BBR_design.md): scope, acquisition requirements, storage sizing, proposed architecture, and verification planning.
- [Business proposal](Aviation_BBR_business_proposal.md): target customers, product pricing, illustrative unit economics, pilot strategy, and development milestones.

## Related repository

This project builds on [BBR](https://github.com/Ala-Ismail/BBR), the private baseline FPGA/VHDL recorder repository. Access to BBR requires permission from its owner; visitors without access may see a GitHub 404 page.

The design study references BBR's [architecture](https://github.com/Ala-Ismail/BBR/blob/main/BBR%20architecture.md) and [development instructions](https://github.com/Ala-Ismail/BBR/blob/main/AGENTS.md). Those documents remain in the private repository. The MIT license in this public repository applies to its contents and does not grant access to or relicense the private BBR repository.

## FPGA and VHDL development

Intel Quartus is the anticipated implementation tool for the proposed MAX 10 target. A VHDL simulator such as GHDL or ModelSim/Questa can support simulation. Tool versions, the VHDL language revision, and reproducible build commands will be recorded when the implementation is added.

Suggested layout as development progresses:

```text
rtl/          Synthesizable VHDL sources
tb/           VHDL testbenches and simulation fixtures
constraints/  Timing constraints and pin assignments
fpga/         FPGA project files and IP configuration
scripts/      Build, simulation, and verification scripts
docs/         Supporting design and verification documentation
build/        Generated outputs (ignored by Git)
```

Commit HDL sources, testbenches, constraints, project settings, IP configuration, memory initialization data, and scripts needed to reproduce a build. The `.gitignore` excludes common Quartus, Vivado, ModelSim/Questa, and GHDL generated files, waveforms, logs, and programming images. Store generated artifacts in `build/` where practical.

Before introducing RTL, define module interfaces, reset and clock behavior, timing requirements, storage formats, and acceptance criteria. Add simulation coverage alongside each implemented function.

## License

Licensed under the [MIT License](LICENSE).
