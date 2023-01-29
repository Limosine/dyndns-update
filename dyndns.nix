
{ lib, buildPythonApplication, fetchgit, requests }:

buildPythonApplication {
  pname = "dyndns-update";
  version = "20230129";
  format = "setuptools";

  src = builtins.fetchGit {
    url = "git@github.com:Limosine/dyndns-update.git";
    rev = "39d7c07b621f4348759b97bfa600b2e8b1153315";
  };

  propagatedBuildInputs = [ requests ];

  doCheck = false;
}
