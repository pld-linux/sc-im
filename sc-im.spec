Summary:	Sc is a free curses-based spreadsheet program that uses key bindings similar to vi and less
Summary(pl.UTF-8):	Sc jest darmowym, bazującym na curses arkuszem kalkulacyjnym, uzywającym skrótów klawiszowych podobnych do vi oraz less
Name:		sc-im
Version:	0.6.0
Release:	2
License:	BSD-like
Group:		Applications/Math
Source0:	https://github.com/andmarti1424/sc-im/archive/v%{version}.zip
# Source0-md5:	2c81f2a6e0cb24b88ff7a2daa7bc585e
URL:		https://github.com/andmarti1424/sc-im
BuildRequires:	libxml2-devel
BuildRequires:	libzip-devel
BuildRequires:	lua51-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	yacc
#BuildRequires:	xlsreader-devel
#BuildRequires:	xlsxwriter-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sc is a spreadsheet calculator based on rectangular tables like a
financial spreadsheet. When invoked it presents you with a table
organized as rows and columns of cells. If invoked without a file
argument, by default the initial table is empty. Each cell can be
associated with a numeric value, a label string and/or an expression
which evaluates to a numeric value or label string, often based on
other cell values (formula).

%description -l pl.UTF-8
Sc jest jest arkuszem kalkulacyjnym bazującym na prostokątnych
tabelkach, takich jak finansowe arkusze. Po odpaleniu zaprezentuje
tabelke zorganizowaną z wierszy i kolumn komórek. Jeżeli zostanie
wywołany bez argumentu plikowego, domyślnie tabelka będzie pusta.
Każdej komórce można przypisać wartość numeryczną, tekstową etykietę
oraz/lub wyrażenie rozwijane do wartości numerycznej lub etykiety
tesktowej, często bazując na wartościach innych komórek (formuła).

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
%{__make} -C src \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HELP KNOWN_ISSUES LICENSE Readme.md USER_REQUESTS WIKI *.png
%attr(755,root,root) %{_bindir}/scim
%{_datadir}/scim
%{_mandir}/man1/scim.1*
