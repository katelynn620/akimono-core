# �M���h�R�}���h���� 2005/01/06 �R��

$NOMENU=1;
$Q{bk}=$Q{er}="gd";
my $usetime=3*60*60;

Lock();
DataRead();
CheckUserPass();
OutError('�M���h�ɓ����Ă��܂���') if !$DT->{guild};
ReadGuild();
ReadGuildData();

my $functionname=$Q{mode};
OutError('bad request') if !defined(&$functionname);
&$functionname;

WriteGuildData();
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
$disp.=$ret;
OutSkin();
1;

sub fund
{
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$DT->{money});

OutError('��t���z���w�肵�Ă�������') if !$count;
OutError('�Œ�ł�'.GetMoneyString(100000).'�͎��X�Ɏc���܂��傤') if ($DT->{money} - $count) < 100000;

$ret="�M���h�u".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."�v��".GetMoneyString($count)."��t";
EditGuildMoney($DT->{guild} ,$count);
$DT->{money}-=$count;
$DT->{paytoday}+=$count;
PushLog(0,0,$DT->{shopname}."���M���h�u".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."�v��".GetMoneyString($count)."��t���܂����B");
}

sub break
{
OutError('�����������Ȃ��Ǝ��s�ł��܂���') if (!$DT->{user}{_so_e});
OutError('���Ԃ�����܂���') if GetStockTime($DT->{time})<$usetime;
UseTime($usetime);
my $tg=$Q{tg};
OutError('�W�I���w�肵�Ă�������') if !$tg;
OutError('���̃M���h�ɑ΂��čU���͂ł��܂���') if ($GUILD_DATA{$tg}->{money} <= $GUILD_DATA{$DT->{guild}}->{money});

$ret="�M���h�u".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."�v�̃u���C�N�B";
my $attack=0;
my $powerdeg=$GUILD_DATA{$DT->{guild}}->{atk} - $GUILD_DATA{$tg}->{def} + int(rand(50));
$attack= int( ($GUILD_DATA{$tg}->{money} + 1000000) * $powerdeg / 1600) if ($powerdeg > 0);

$GUILD_DATA{$DT->{guild}}->{atk}=int($GUILD_DATA{$DT->{guild}}->{atk} *9 /10);
$GUILD_DATA{$tg}->{def}=int($GUILD_DATA{$tg}->{def} *4 /5);

$ret.="�������u".$GUILD{$tg}->[$GUILDIDX_name]."�v�͖h��I",PushLog(2,0,$ret),return if (!$attack);

$ret.="�u".$GUILD{$tg}->[$GUILDIDX_name]."�v����".GetMoneyString($attack)."��D��I";
EditGuildMoney($tg ,-$attack);
PushLog(2,0,$ret);

$income=int($attack / 10) + 1000;
$attack=int($attack * 9 / 10);
EditGuildMoney($DT->{guild} ,$attack);
$DT->{money}+=$income;
$DT->{saletoday}+=$income;
PushLog(0,$DT->{id},"�u���C�N�����̕񏧋��Ƃ���".GetMoneyString($income)."����B");
$ret.="<br>�u���C�N�����̕񏧋��Ƃ���".GetMoneyString($income)."����B";
if ($GUILD_DATA{$tg}->{money} < 0)
	{
	unlink($COMMON_DIR."/".$tg.".pl") ;
	$GUILD_DATA{$DT->{guild}}->{def}=int($GUILD_DATA{$DT->{guild}}->{def} * 3 / 2);
	$GUILD_DATA{$DT->{guild}}->{def}=1000 if ($GUILD_DATA{$DT->{guild}}->{def} > 1000);
	}
}

sub force
{
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError('bad request') if (!$ckeckok);
OutError('�����������Ȃ��Ǝ��s�ł��܂���') if (!$DT->{user}{_so_e});
OutError('���Ԃ�����܂���') if GetStockTime($DT->{time})<$usetime;
UseTime($usetime);
OutError('�����̕K�v������܂���') if ($GUILD_DATA{$DT->{guild}}->{atk} > 990);
my $guild=$GUILD_DATA{$DT->{guild}};
my $cnt=int($guild->{money} / 4);
$guild->{money} -= $cnt;
$guild->{atk} += int($cnt/25000);
$guild->{atk} = 1000 if $guild->{atk} > 1000;
$ret = "�M���h�u".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."�v���R���𑝋����܂����B";
PushLog(0,0,$ret);
}

