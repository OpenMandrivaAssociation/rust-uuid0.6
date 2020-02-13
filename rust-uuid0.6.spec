# Generated by rust2rpm 12
%bcond_without check
%global debug_package %{nil}

%global crate uuid

Name:           rust-%{crate}0.6
Version:        0.6.5
Release:        3%{?dist}
Summary:        Library to generate and parse UUIDs

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/uuid
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to generate and parse UUIDs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+byteorder-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+byteorder-devel %{_description}

This package contains library source intended for building other packages
which use "byteorder" feature of "%{crate}" crate.

%files       -n %{name}+byteorder-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+const_fn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+const_fn-devel %{_description}

This package contains library source intended for building other packages
which use "const_fn" feature of "%{crate}" crate.

%files       -n %{name}+const_fn-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+md5-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+md5-devel %{_description}

This package contains library source intended for building other packages
which use "md5" feature of "%{crate}" crate.

%files       -n %{name}+md5-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages
which use "rand" feature of "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sha1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sha1-devel %{_description}

This package contains library source intended for building other packages
which use "sha1" feature of "%{crate}" crate.

%files       -n %{name}+sha1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+slog-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+slog-devel %{_description}

This package contains library source intended for building other packages
which use "slog" feature of "%{crate}" crate.

%files       -n %{name}+slog-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+u128-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+u128-devel %{_description}

This package contains library source intended for building other packages
which use "u128" feature of "%{crate}" crate.

%files       -n %{name}+u128-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+use_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_std-devel %{_description}

This package contains library source intended for building other packages
which use "use_std" feature of "%{crate}" crate.

%files       -n %{name}+use_std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1-devel %{_description}

This package contains library source intended for building other packages
which use "v1" feature of "%{crate}" crate.

%files       -n %{name}+v1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v3-devel %{_description}

This package contains library source intended for building other packages
which use "v3" feature of "%{crate}" crate.

%files       -n %{name}+v3-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v4-devel %{_description}

This package contains library source intended for building other packages
which use "v4" feature of "%{crate}" crate.

%files       -n %{name}+v4-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v5-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v5-devel %{_description}

This package contains library source intended for building other packages
which use "v5" feature of "%{crate}" crate.

%files       -n %{name}+v5-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 20:32:42 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.5-2
- Initial package
