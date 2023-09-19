{ lib, fetchFromGitHub, buildPythonPackage, pythonOlder, requests }:

buildPythonPackage rec {
  pname = "dyndns-update";
  version = "20230205";
  format = "setuptools";

  disabled = pythonOlder "3.10";

  src = fetchFromGitHub {
    owner = "Limosine";
    repo = "dyndns-update";
    rev = "bd07027f505a0108843848875d3b89b7403c6511";
    sha256 = "sha256-3xsIKAEbIJlFFqFoCgt1rfD+/ngwdyI8fA/CfNqFHBU=";
  };

  propagatedBuildInputs = [ requests ];

  pythonImportsCheck = [ "dyndns_update" ];

  doCheck = false;

  meta = with lib; {
    description = "Update your DynDNS hosts";
    homepage = "https://github.com/Limosine/dyndns-update";
  };
}
