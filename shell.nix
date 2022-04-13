# shell.nix
{ pkgs ? import <nixpkgs> {} }:
let
  my-python = pkgs.python310;
  python-with-my-packages = my-python.withPackages (p: with p; [
    requests
    # other python packages you want
  ]);
in
pkgs.mkShell {
  buildInputs = [
    python-with-my-packages
    pkgs.poetry
    # other dependencies
  ];
  shellHook = ''
    PYTHONPATH=${python-with-my-packages}/${python-with-my-packages.sitePackages}
	echo "Welcome to Nix!"
	IN_NIX_SHELL=True
	source $HOME/.poetry/env
    # maybe set more env-vars
  '';
}

