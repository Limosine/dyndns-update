
{ lib, buildPythonApplication, fetchgit, requests, pytest }:

# with import <nixpkgs> {};
# with pkgs.python3Packages;

# let
#   pkgs = import nixpkgs {};
# in

buildPythonApplication {
  pname = "dyndns-update";
  version = "20230129";
  format = "setuptools";

  src = ./.;
  # src = pkgs.fetchgitPrivate /home/quentin/.ssh/id_ed25519 {
  #   url = "ssh://pi@raspberrypi/srv/git/dyndns.git";
  #   rev = "4478096a60f360c9675da7a1264372129916a523";
  # };

  propagatedBuildInputs = [ requests ];

  doCheck = false;

  # checkInputs = [ pytest ];

  # checkPhase = ''
  #   pytest
  # '';
}
