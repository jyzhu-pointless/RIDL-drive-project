# RIDL-drive modeling project

## SLiM Model description

SLiM models used in this project are included.

## Data description

The `*.csv` files in the raw data adhere to the following naming convention:

```txt
[Transgene type]_[Param 1]-[Param 1 value]-[Param 2]-[Param 2 value]-..._[Repetition number].csv
```

where:

- `[Transgene type]` indicates the type of transgene element applied in the simulation. It should be `FLAD` (Drive-RIDL), `TARE`, `FLADSPLIT`, `RIDL`, or `SIT`.
- `[Param]`s and `[Param value]`s indicate some important parameters and their values in the simulation. Here are some `[Param]`s:
  - `drop`: drop ratio (a positive float number in)
  - `eff`: drive efficiency (a float number in $[0.0,1.0]$)
  - `fit`: drive (RIDL/SIT) homozygotes fitness (a float number in $[0.5,1.0]$)
  - `ldgr`: low-density growth rate (a float positive number)
  - `r2`: germline resistance rate (a float number in $[0.0,0.5]$)
  - `hets`: heterozygotes survival rate (a float number in $[0.0,0.5]$)
  - `curve`: density-dependent growth curve type ( `concave` / `linear` / `convex` )
  - `type`: rescue drive type ( `normal` / `haplolethal` / `recessivelethal` )
- `[Repetition number]` is a positive integer (1~20), representing one of the 20 simulations with identical parameters.
