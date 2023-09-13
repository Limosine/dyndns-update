{ lib, fetchFromGitHub, buildPythonPackage, pythonOlder, requests }:

buildPythonPackage rec {
  pname = "dyndns-update";
  version = "20230205";
  format = "setuptools";

  disabled = pythonOlder "3.10";

  src = fetchFromGitHub {
    owner = "Limosine";
    repo = "dyndns-update";
    rev = "6c0c35dba76c5e00ccf708a6c6eab954cb39192a";
    sha256 = "sha256-pXpwOogjd4DYJfI9Qvh6u4e36TNlmoNkYJPPhwxc/Q0=";
  };

  propagatedBuildInputs = [ requests ];

  pythonImportsCheck = [ "dyndns_update" ];

  doCheck = false;

  meta = with lib; {
    description = "Update your DynDNS hosts";
    homepage = "https://github.com/Limosine/dyndns-update";
  };
}
