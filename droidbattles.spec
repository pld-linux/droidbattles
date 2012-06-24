Summary:	A game of programming
Summary(pl.UTF-8):	Gra w programowanie
Name:		droidbattles
Version:	1.0.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.bluefire.nu/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	88f71cc17895d3aa77cfbb3428d41dbc
Source1:	http://www.bluefire.nu/%{name}/bots-light-01-06-11.tar.gz
# Source1-md5:	358a931c2d795f6c005a9b4da07c1439
Source2:	%{name}.desktop
Source3:	%{name}.png
URL:		http://www.bluefire.nu/droidbattles/
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
So, you're having this argument about who's the best programmer? Or
you just want to have some programming fun? What better way to do it
than a little game of AI programming.

In DroidBattles you design the bots by choosing which hardware they
should contain. Each bot can have up to 32 hardware devices that you
can choose freely from a list of available types. Examples include
weapons, armor, CPU:s, engines... etc.

When you have chosen the hardware it's time to program it. You make a
program (in an assembler like language) that is loaded into a virtual
RAM of the bot and then executed by the CPU device(s) you've included
with the bot. You communicate with your devices through simple in/out
instruktions.

Other features of DroidBattles includes team-battle and set up of
"rules" for a game, (you can enable/disable hardware devices and also
set the costs).

You can make the bot have it's own graphics that is shown when the
simulation runs. When everyhing is ready you assemble the program and
a .bot file is created. You can now test this bot against other bots
in the simulator, and hopefully your bot will crush it's opponents.

%description -l pl.UTF-8
A więc spierasz się o to, kto jest najlepszym programistą? Lub po
prostu chcesz zaznać przyjemności programowania? Cóż lepszego może być
od gry, w której programujesz Sztuczną Inteligencję.

W DroidBattles projektujesz boty wybierając jaki hardware powinny
zawierać. Każdy bot może pomieścić do 32 urządzeń sprzętowych, które
możesz dowolnie wybierać z dostępnej listy. Mogą to być bronie,
pancerz, CPU, silniki... etc.

Gdy wybrałeś już sprzęt, nadszedł czas na zaprogramowanie. Tworzysz
program (w języku podobnym do assemblera), który jest ładowany do
wirtualnego RAMu bota, a następnie wykonywany przez jednostki
przetwarzania, które zainstalowałeś w bocie. Komunikujesz się ze
swoimi urządzeniami za pomocą prostych instrukcji wejścia/wyjścia.

Wśród innych zalet DroidBattles można wymienić bitwy drużynowe, jak i
zestawy "zasad" dla gry (możesz włączać/wyłączać urządzenia sprzętowe,
a także ustawiać koszt.)

Możesz stworzyć dla bota jego własną grafikę, która będzie pokazywana
podczas symulacji. Gdy wszystko jest gotowe, assemblujesz program i
utworzony zostaje plik .bot. Możesz wtedy przetestować bota w starciu
z innymi botami w symulatorze i przy dozie szczęścia zostać zwycięzcą.

%prep
%setup -q
mkdir bots
cd bots
tar zxvf %{SOURCE1}

%build
find . -exec touch \{\} \;
%configure2_13 \
	--enable-final

cd %{name}
cat installdir.cpp | sed 's@/usr/local/droidbattles@%{_datadir}/droidbattles@' > installdir.cpp.new
mv -f installdir.cpp.new installdir.cpp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

cd %{name}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm docs/en/Makefile*
cd ..
for i in bots/*
do
	mv $i $RPM_BUILD_ROOT/usr/local/%{name}/bots/
done
cd $RPM_BUILD_ROOT/usr
mv local/%{name} X11R6/share/
rm -rf X11R6/share/%{name}/doc
ln -s /usr/share/doc/%{name}-%{version} X11R6/share/%{name}/doc

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%doc %{name}/docs/en/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/droidbattles
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
