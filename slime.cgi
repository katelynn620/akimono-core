# �h���S�����[�X 2005/03/30 �R��

$NOITEM=1;
RequireFile('inc-dragon.cgi');
DragonLasttime();

DataRead();
CheckUserPass(1);
RequireFile("inc-dr-edit".$drlock.".cgi") if ($drlock);

$disp.=GetMenuTag('slime',		'[�����X�|]','&mode=info')
	.GetMenuTag('slime',		'[�o�����[�X]','&mode=rd')
	.GetMenuTag('slime',		'[�d�܃��[�X]','&mode=rd&code=1');
if (!$GUEST_USER)
	{
	$disp.=GetMenuTag('slime',		'[�q��]','&mode=ranch')
		.GetMenuTag('slime',		'[�X��]','&mode=stable')
		.GetMenuTag('slime',		'[�R��]','&mode=jock');
	}
$disp.="<hr width=500 noshade size=1>";
$Q{mode}||="info";
RequireFile("inc-dragon-$Q{mode}.cgi");
OutSkin();
1;

sub DragonLasttime
{
undef @DRTIME;
$drlock=0;
my $fn=GetPath($COMMON_DIR,"dr-last");
if (-e $fn)
	{
	require $fn;
	$drlock=2 if ($NOW_TIME > $DRTIME[1] || $NOW_TIME > $DRTIME[2]);
	$drlock=1 if ($NOW_TIME > $DRTIME[0]);
	CoLock() if $drlock;
	}
	else
	{
	#�X�V���������ݒ�
	CoLock();
	foreach(0..2) { $DRTIME[$_]=$NOW_TIME + 86400 -(($NOW_TIME + $TZ_JST - $DRTIMESET[$_] * 3600) % 86400); }
	WriteDrLast();
	CoDataCA();
	CoUnLock();
	}
}

