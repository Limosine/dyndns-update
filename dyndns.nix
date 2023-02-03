
{ lib, buildPythonPackage, pythonOlder, requests }:

buildPythonPackage rec {
  pname = "dyndns-update";
  version = "20230129";
  format = "setuptools";

  disabled = pythonOlder "3.10";

  src = builtins.fetchGit {
    url = "git@github.com:Limosine/dyndns-update.git";
    rev = "ad24d3f25cea7440e30b1497cdc73052cacaaac3";
  };

  propagatedBuildInputs = [ requests ];

  pythonImportsCheck = [ "dyndns_update" ];

  doCheck = false;

  meta = with lib; {
    description = "Update your DynDNS hosts";
    homepage = "https://github.com/Limosine/dyndns-update";
  };
}
