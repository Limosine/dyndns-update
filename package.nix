{ lib, fetchFromGitHub, buildPythonPackage, pythonOlder, requests }:

buildPythonPackage rec {
  pname = "dyndns-update";
  version = "20230512";
  format = "setuptools";

  disabled = pythonOlder "3.10";

  src = ./.;

  propagatedBuildInputs = [ requests ];

  pythonImportsCheck = [ "dyndns_update" ];

  doCheck = false;

  meta = with lib; {
    description = "Update your DynDNS hosts";
    homepage = "https://github.com/Limosine/dyndns-update";
  };
}
