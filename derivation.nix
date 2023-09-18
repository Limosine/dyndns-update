{ lib, fetchFromGitHub, buildPythonPackage, pythonOlder, requests }:

buildPythonPackage rec {
  pname = "dyndns-update";
  version = "20230205";
  format = "setuptools";

  disabled = pythonOlder "3.10";

  src = fetchFromGitHub {
    owner = "Limosine";
    repo = "dyndns-update";
    rev = "5b81cd580ec4fe900885c0beb9ed9de5c8fd16b4";
    sha256 = "sha256-Ow52OKH1HiEzGHE0//+0LBHJ0OOxjyY23SXCpGJ+KXg=";
  };

  propagatedBuildInputs = [ requests ];

  pythonImportsCheck = [ "dyndns_update" ];

  doCheck = false;

  meta = with lib; {
    description = "Update your DynDNS hosts";
    homepage = "https://github.com/Limosine/dyndns-update";
  };
}
