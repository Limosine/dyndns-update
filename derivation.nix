{ lib, buildPythonPackage, pythonOlder, requests }:

buildPythonPackage rec {
  pname = "dyndns-update";
  version = "20230205";
  format = "setuptools";

  disabled = pythonOlder "3.10";

  src = builtins.fetchGit {
    url = "git@github.com:Limosine/dyndns-update.git";
    rev = "2a141c998d9bdb718b2fe4dfe77c54d4fc170bb4";
  };

  propagatedBuildInputs = [ requests ];

  pythonImportsCheck = [ "dyndns_update" ];

  doCheck = false;

  meta = with lib; {
    description = "Update your DynDNS hosts";
    homepage = "https://github.com/Limosine/dyndns-update";
  };
}
