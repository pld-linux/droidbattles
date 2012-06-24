Summary:	A game of programming
Summary(pl):	Gra w programowanie
Name:		droidbattles
Version:	1.0.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.bluefire.nu/%{name}/%{name}-%{version}.tar.gz
Source1:	http://www.bluefire.nu/%{name}/bots-light-01-06-11.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}.png
URL:		http://www.bluefire.nu/droidbattles/
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

%description -l pl
A wi�c spierasz si� o to, kto jest najlepszym programist�? Lub po
prostu chcesz zazna� przyjemno�ci programowania? C� lepszego mo�e by�
od gry, w kt�rej programujesz Sztuczn� Inteligencj�.

W DroidBattles projektujesz boty wybieraj�c jaki hardware powinny
zawiera�. Ka�dy bot mo�e pomie�ci� do 32 urz�dze� sprz�towych, kt�re
mo�esz dowolnie wybiera� z dost�pnej listy. Mog� to by� bronie,
pancerz, CPU, silniki... etc.

Gdy wybra�e� ju� sprz�t, nadszed� czas na zaprogramowanie. Tworzysz
program (w j�zyku podobnym do assemblera), kt�ry jest �adowany do
wirtualnego RAMu bota, a nast�pnie wykonywany przez jednostki
przetwarzania, kt�re zainstalowa�e� w bocie. Komunikujesz si� ze
swoimi urz�dzeniami za pomoc� prostych instrukcji wej�cia/wyj�cia.

W�r�d innych zalet DroidBattles mo�na wymieni� bitwy dru�ynowe, jak i
zestawy "zasad" dla gry (mo�esz w��cza�/wy��cza� urz�dzenia sprz�towe,
a tak�e ustawia� koszt.)

Mo�esz stworzy� dla bota jego w�asn� grafik�, kt�ra b�dzie pokazywana
podczas symulacji. Gdy wszystko jest gotowe, assemblujesz program i
utworzony zostaje plik .bot. Mo�esz wtedy przetestowa� bota w starciu
z innymi botami w symulatorze i przy dozie szcz�cia zosta� zwyci�zc�.

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

gzip -9nf AUTHORS ChangeLog TODO

cd %{name}
%{__make} install DESTDIR=$RPM_BUILD_ROOT
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
%doc *.gz
%doc %{name}/docs/en/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/droidbattles
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
