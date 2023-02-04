
{ lib, buildPythonPackage, pythonOlder, requests }:

buildPythonPackage rec {
  pname = "dyndns-update";
  version = "20230129";
  format = "setuptools";

  disabled = pythonOlder "3.10";

  src = builtins.fetchGit {
    url = "git@github.com:Limosine/dyndns-update.git";
    rev = "91e39d2f510e056684edec7bd4370b7deea54d1a";
  };

  propagatedBuildInputs = [ requests ];

  pythonImportsCheck = [ "dyndns_update" ];

  doCheck = false;

  meta = with lib; {
    description = "Update your DynDNS hosts";
    homepage = "https://github.com/Limosine/dyndns-update";
  };
}
