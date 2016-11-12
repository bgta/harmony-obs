#
# spec file for package rambox
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           harmony
Version:        0.4.2
Release:        0
Summary:        Sleek music player for Spotify, SoundCloud, Google Play Music and your local files
License:        MIT
Group:          Productivity/AudioVideo/Music/Player/Jukebox
Url:            http://getharmony.xyz/
ExclusiveArch:  x86_64 %ix86
Source0:        https://github.com/vincelwt/harmony/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.sh
Source4:        %{name}.1

BuildRequires:  update-desktop-files
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
Sleek music player for Spotify, SoundCloud, Google Play Music and your local files.

%prep
%setup -q

%build

%install
install -d %{buildroot}/{opt/%{name},usr/{bin,share/{pixmaps,man/man1}}}
cp -R * %{buildroot}/opt/%{name}
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE4} %{buildroot}%{_datadir}/man/man1
%suse_update_desktop_file -i %{name}
chmod +x %{buildroot}/opt/%{name}/Harmony

# Let's use %%doc macro.
rm %{buildroot}/opt/%{name}/LICENSE*
for i in `find %{buildroot}/opt/%{name}/resources/app/node_modules -type f -name "*.h"`;do rm -f $i;done
for i in `find %{buildroot}/opt/%{name}/resources/app/node_modules -type f -name "*.cpp"`;do rm -f $i;done

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc LICENSE*
/opt/%{name}
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*.?.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
