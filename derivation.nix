{ lib, fetchFromGitHub, buildPythonPackage, pythonOlder, requests }:

buildPythonPackage rec {
  pname = "dyndns-update";
  version = "20230205";
  format = "setuptools";

  disabled = pythonOlder "3.10";

  src = fetchFromGitHub {
    owner = "Limosine";
    repo = "dyndns-update";
    rev = "25d90fdc58410373fdc9fab12a1dae6030ca1ecd";
    sha256 = "sha256-CabzHIkSZMoMJGCRa4FBNq4JEGyFDW96ukLQzKm1HfQ=";
  };

  propagatedBuildInputs = [ requests ];

  pythonImportsCheck = [ "dyndns_update" ];

  doCheck = false;

  meta = with lib; {
    description = "Update your DynDNS hosts";
    homepage = "https://github.com/Limosine/dyndns-update";
  };
}
