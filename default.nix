{ pkgs ? import <nixpkgs> {} }:
pkgs.python3Packages.callPackage ./dyndns.nix {}
