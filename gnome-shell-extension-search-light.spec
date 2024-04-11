%global uuid search-light@icedman.github.com

Name:        gnome-shell-extension-search-light
Version:     {{{ git_dir_version }}}
Release:     1%{?dist}
Summary:     Take the apps search out of overview

Group:       User Interface/Desktops
License:     GPLv3
URL:         https://github.com/KyleGospo/search-light
Source0:     %{url}/archive/refs/heads/main.tar.gz
BuildArch:   noarch

Requires:    gnome-shell >= 3.12

BuildRequires: make
BuildRequires: glib2

%description
This is a Gnome Shell extension that takes the apps search widget out of Overview. Like the macOS spotlight, or Alfred.

%prep
%autosetup -n search-light-main

%build
make build
# Nothing to build

%install
make publish
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
unzip -q %{uuid}.zip -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}