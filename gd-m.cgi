# �M���h���c 2004/01/20 �R��

CoLock() if ($Q{edit});
Lock() if ($Q{edit} eq "join");
DataRead();
CheckUserPass();
RequireFile('inc-gd.cgi');

@ENTRYnamelist=qw(
		no tm town id guild
		);
ReadEntry();

$Q{er}='gd';
RequireFile('inc-gd-entry.cgi') if ($Q{edit});
my $functionname=$Q{mode};
$functionname||="join";
OutError("bad request") if !defined(&$functionname);
&$functionname;

OutSkin();
1;


sub join
{
OutError("bad request") if ($DT->{guild});
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�M���h��t</SPAN>�F���c����ɂ́C�c���܂��͌R�t�̋����K�v�ł��B<br>
���肽���M���h�̓��c�������Q�Ƃ��C�₢���킹�Ă݂�Ƃ悢�ł��傤�B
$TRE$TBE<br>
HTML
$disp.="�M���h�풆�͓��c�ł��܂���",return if ($DTevent{guildbattle});
my $join="";
	foreach my $cnt(0..$Ecount)
		{
		next if ($ENTRY[$cnt]->{town} ne $MYDIR || $ENTRY[$cnt]->{id} != $DT->{id});
		my $guild=$ENTRY[$cnt]->{guild};
$join.=<<"HTML";
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<BIG>��$GUILD_DETAIL{$guild}->{shortname}</BIG>�F���c�����o�Ă��܂��B 
<INPUT TYPE=HIDDEN NAME=edit VALUE="join">
<INPUT TYPE=HIDDEN NAME=guild VALUE="$guild">
<INPUT TYPE=SUBMIT VALUE="���c����">
</form><br>
HTML
	}
$disp.=($join) ? $join : "���c�����o�Ă��܂���";
}

sub submit
{
OutError("bad request") if (!$DT->{guild});
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError("bad request") if (!$ckeckok);

ReadLetterName();
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�M���h��t</SPAN>�F�N�̓��c�������܂����H<br>
��x������ƁC�P��͂ł��Ȃ��̂ł����ӂ��������B
$TRE$TBE<br>
HTML
$disp.="�M���h�풆�͋��ł��܂���",return if ($DTevent{guildbattle});
EntryList() if scalar(@MYENTRY);
EntryForm();
}

sub EntryList
{
	$disp.=<<"HTML";
$TB$TR
$TDB�X��
$TDB�����X
$TDB�L������
$TRE
HTML

foreach my $i(@MYENTRY)
	{
	my($no,$town,$id)=($ENTRY[$i]->{no},$ENTRY[$i]->{town},$ENTRY[$i]->{id});
	my $sname=SearchLetterName($id,$town);
	$disp.=$TR.$TD.$sname;
	$disp.=$TD.$Tname{$town};
	$disp.="$TD����".GetTime2HMS($ENTRY[$i]->{tm}-$NOW_TIME);
	}
$disp.=$TRE.$TBE."<br>";
}

sub EntryForm
{
$disp.=<<"HTML";
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
$TB
$TR$TDB<b>���c����</b>�i�����ꂩ�P�j
HTML

my $r=int(scalar(@OtherDir) / 2 + 0.5);$r||=1;
foreach(0..$#OtherDir)
	{
	my $pg=$OtherDir[$_];
	$disp.=( ($_ % $r) ? "<br>" : $TD);
	$disp.="$Tname{$pg} <SELECT NAME=$pg><OPTION VALUE=\"\">�I��";
	foreach my $i(0..$Ncount{$pg})
		{
		$disp.="<OPTION VALUE=\"$LID{$pg}[$i]\"".($Q{$pg}==$LID{$pg}[$i] ? ' SELECTED' : '').">$LNAME{$pg}[$i]";
		}
	$disp.="</SELECT>\n";
	}
$disp.=<<"HTML";
$TRE$TBE
<br><INPUT TYPE=HIDDEN NAME=edit VALUE="new">
<INPUT TYPE=SUBMIT VALUE="���c��������">
</FORM>
HTML
}

sub joind
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�M���h��t</SPAN>�F���c�葱���������܂����B<br>
�M���h�̍�펺�Ȃǂł��������Ă����Ƃ悢�ł��傤�B
$TRE$TBE<br>
HTML
}

sub ReadEntry
{
	undef @ENTRY;
	undef @MYENTRY;
	open(IN,GetPath($COMMON_DIR,"entry")) or return;
	my @ent=<IN>;
	close(IN);
	$Ecount=$#ent;
	return if $Ecount < 0;
	foreach my $cnt(0..$Ecount)
		{
		chop $ent[$cnt];
		my @buf=split(/,/,$ent[$cnt]); my $i=0;
		foreach (@ENTRYnamelist) { $ENTRY[$cnt]->{$_}=$buf[$i];$i++;}
		undef $ENTRY[$cnt],next if ($ENTRY[$cnt]->{tm} < $NOW_TIME);	# �����؂���폜�B
		push(@MYENTRY, $cnt) if ($ENTRY[$cnt]->{guild} eq $DT->{guild});
	}
}

