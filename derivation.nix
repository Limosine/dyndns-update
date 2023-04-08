{ lib, fetchFromGitHub, buildPythonPackage, pythonOlder, requests }:

buildPythonPackage rec {
  pname = "dyndns-update";
  version = "20230205";
  format = "setuptools";

  disabled = pythonOlder "3.10";

  src = fetchFromGitHub {
    owner = "Limosine";
    repo = "dyndns-update";
    rev = "babe3ea5aa71eb3386735e93193e86c396087c49";
    sha256 = "sha256-Wqyd6ujUEcPcBV6kbf3gMvHLR2dnXUgIl2CX/nPD8NI=";
  };

  propagatedBuildInputs = [ requests ];

  pythonImportsCheck = [ "dyndns_update" ];

  doCheck = false;

  meta = with lib; {
    description = "Update your DynDNS hosts";
    homepage = "https://github.com/Limosine/dyndns-update";
  };
}
