# ���m�ٗp�������� 2005/01/06 �R��

$NOMENU=1;
Lock();
DataRead();
CheckUserPass();
ReadArmy();

my $functionname=$Q{mode};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteArmy();
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

$disp.=$TBT.$TRT.$TD.GetTagImgJob($DT->{job},$DT->{icon});
$disp.=$TD.GetMenuTag('army',	'[�b������]');
$disp.=GetMenuTag('main','[���X�ɖ߂�]');
$disp.=$TRE.$TBE;
$disp.="<br>".$ret;
OutSkin();
1;


sub plus
{
my $limit=($DT->{dignity}+0)*1000 - $ARMY{$DT->{id}};
my $price=($DTevent{rebel}) ? 1500 : 1000;
my $usetime=60*40;
UseTime($usetime);

$num=CheckCount($Q{cnt1},$Q{cnt2},0,$limit);
OutError('���ʂ��w�肵�Ă��������B') if !$num;

$num=int($DT->{money}/$price) if $DT->{money}<$num*$price;
$num=0 if $num<0;
OutError('����������܂���B') if !$num;

$ARMY{$DT->{id}}+=$num;
$DT->{money}-=$num*$price;

$ret="���m���ԏ��ɂăh���[�t���m��".$num."�l@".GetMoneyString($price)."(�v".GetMoneyString($price*$num).")�ɂČق��܂���";
$ret.="/".GetTime2HMS($usetime)."����";
PushLog(0,$DT->{id},$ret);
}

sub fire
{
$num=CheckCount($Q{cnt1},$Q{cnt2},0,$ARMY{$DT->{id}});
OutError('���ʂ��w�肵�Ă��������B') if !$num;

my $usetime=60*10;
UseTime($usetime);
$ARMY{$DT->{id}}-=$num;

$ret="�h���[�t���m��".$num."�l���ق��܂���";
$ret.="/".GetTime2HMS($usetime)."����";
PushLog(0,$DT->{id},$ret);
}

sub rebelon
{
OutError('�������J�n����ɂ� rebel �Ɠ��͂��Ă��������B') if ($Q{cmd} ne "rebel");
OutError('���m��������܂���B') if ($ARMY{$DT->{id}} < 2500);

my $usetime=60*30;
UseTime($usetime);
$DTevent{rebel}=$NOW_TIME+86400*3;
$RIOT{$DT->{id}}=1;
$STATE->{safety}=int($STATE->{safety} * 9 / 10) if ($STATE->{safety} > 5000);

$ret="�h���[�t���m�������I�N�B�������n�܂�܂����I";
PushLog(2,0,$DT->{shopname}."�̎w����".$ret);
$ret.="/".GetTime2HMS($usetime)."����";
}

sub rside
{
OutError('�����Ɍĉ�����ɂ� rebel �Ɠ��͂��Ă��������B') if ($Q{cmd} ne "rebel");

my $usetime=60*20;
UseTime($usetime);
$RIOT{$DT->{id}}=1;

$ret="�����Ɍĉ����C�Q�킵�܂����I";
PushLog(3,0,$DT->{shopname}."��".$ret);
$ret.="/".GetTime2HMS($usetime)."����";
}

sub lside
{
OutError('�����ɎQ�����Ȃ���̎�̖��������邱�Ƃ͂ł��܂���B') if ($RIOT{$DT->{id}});

my $usetime=60*20;
UseTime($usetime);
if ($STATE->{leader}==$DT->{id})
	{
	$STATE->{army}+=$ARMY{$DT->{id}};
	}
	else
	{
	$STATE->{robina}+=$ARMY{$DT->{id}};
	PushLog(3,0,$DT->{shopname}.'�͗̎�ɖ������C�`�E����h�����܂����B');
	}

delete $ARMY{$DT->{id}};
$ret="���m��̎�̌�q�R�ɔh�����܂���";
$ret.="/".GetTime2HMS($usetime)."����";
}
