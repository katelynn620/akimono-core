# �����Ǘ� 2005/03/30 �R��

Lock() if $Q{mode};
$image[0]=GetTagImgKao("��b","minister",'align="left" ');
DataRead();
CheckUserPass();
OutError('�����Ǘ����s����̂͗̎�݂̂ł�') if $STATE->{leader}!=$DT->{id};
RequireFile('inc-manor.cgi');

ReadDTSub($DT,"lord");
my $functionname=$Q{mode};
&$functionname if defined(&$functionname);


# �����ݒ���擾
my $MANORLORD=$DT->{_lord};

my $shoplist="";
my $taxsum=0;
foreach (@DT) {
$shoplist.="<OPTION VALUE=\"$_->{id}\">$_->{shopname}";
$taxsum+=$_->{taxtoday};
}

my $now=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;
my $ii=($now % $ONE_DAY_TIME);
$ii=1 if $ii < 1;
$taxsum=GetMoneyString(int($taxsum * $ONE_DAY_TIME / $ii / 10000) * 10000);

$disp.="<BIG>�������Ǘ���</BIG><br><br>";
$disp.=$TB.$TR.$TD.$image[0]."<SPAN>��b</SPAN>�F������ԂɋC�����ĉ^�c���Ȃ��Ƃ����܂��񂼁B<br>";
$disp.="�E�̔��݌ɂ́C��x�ɂ� 1000�܂ŁB<br>";
$disp.="�E��̔̔����i�́C".GetMoneyString(1000)." �` ".GetMoneyString(10000)."�B<br>";
$disp.="�E���n���̔��承�i�́C".GetMoneyString(5000)." �` ".GetMoneyString(40000)."�B<br>";
$disp.="�E�̔����i�𔃎承�i��荂������ƁC�N���g��������܂���̂ł����ӂ��B".$TRE.$TBE;

$disp.="<hr width=500 noshade size=1><BIG>�����݂̍������</BIG><br><br>";
$disp.="$TB$TDB�X����$TDB�Ŏ�������$TDB�O���Ŏ�$TDB�O���Ώo$TRE";
$disp.=$TR.$TD.GetMoneyString($STATE->{money}).$TD.$taxsum;
$disp.=$TD.GetMoneyString($STATE->{in}).$TD.GetMoneyString($STATE->{out}).$TRE.$TBE;


$disp.=<<"HTML";
<hr width=500 noshade size=1><BIG>�������ݒ�</BIG><br><br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="inside">
$TB$TR
$TDB��$TDB�̔��݌�$TDB�̔����i$TD$TDB���n��$TDB���承�i$TDB���������$TDB����$TRE
HTML

my $balance=0;
foreach my $i(0..$#MANOR)
	{
	my @MYMANOR=@{$MANOR[$i]};
	$disp.=$TR.$TD.GetTagImgManor($MYMANOR[1]).$MYMANOR[0];
	my $c=$MANORLORD->{"count$i"} + 0;
	$disp.=qq|$TD<INPUT TYPE=TEXT NAME=count$i SIZE=8 VALUE="$c"> ��|;
	my $t=$MANORLORD->{"price$i"} + 0;
	$balance-=$c*$t;
	$disp.=$TD."@".qq|$term[0]<INPUT TYPE=TEXT NAME=price$i SIZE=8 VALUE="$t">$term[1]|;
	$disp.=$TD."��".$TD.GetTagImgManor($MYMANOR[3]).$MYMANOR[2];
	$t=$MANORLORD->{"cost$i"} + 0;
	$balance+=$c*$t;
	$disp.=$TD."@".qq|$term[0]<INPUT TYPE=TEXT NAME=cost$i SIZE=8 VALUE="$t">$term[1]|;
	$disp.=$TD.($MANORLORD->{"stock$i"} +0)." ��";
	$disp.=$TD."<small>���搔 $MYMANOR[5]��".GetTagImgItemType($MYMANOR[4]).$ITEM[$MYMANOR[4]]->{name}."�𐶐�</small>".$TRE;
	}
$disp.=$TBE."<br>����L�̑����ݒ�ł́C".GetMoneyString($balance)."�̍����x�o�������܂�܂��B<br><br>";

$disp.=<<"HTML";
<INPUT TYPE=SUBMIT VALUE="�ȏ�̓��e�Ō���">
</FORM>
<hr width=500 noshade size=1>
	<FORM ACTION="action.cgi" $METHOD>
	$MYFORM$USERPASSFORM
	<INPUT TYPE=hidden NAME=mode VALUE="outside">
<BIG>���Y������</BIG>�F ������������n������Y���� 
<INPUT TYPE=SUBMIT VALUE="��������">
	</FORM>
HTML

OutSkin();
1;


sub inside
{
foreach my $i(0..$#MANOR)
	{
	$DT->{_lord}->{"count$i"}=CheckCount($Q{"count$i"},0,0,1000);
	$DT->{_lord}->{"price$i"}=CheckCount($Q{"price$i"},0,1000,10000);
	$DT->{_lord}->{"cost$i"}=CheckCount($Q{"cost$i"},0,5000,40000);
	}
WriteDTSub($DT,"lord");
DataCommitOrAbort();
UnLock();
}

sub outside
{
my $flag=0;
foreach my $i(0..$#MANOR)
	{
	my @MYMANOR=@{$MANOR[$i]};
	my $num=0;
	$num=int($DT->{_lord}->{"stock$i"} / $MYMANOR[5]) if $MYMANOR[5];
	next if !$num;	#�����\���Ȃ�

	my $itemno=$MYMANOR[4];
	my $count=CheckCount($num,0,0,$ITEM[$itemno]->{limit} - $DT->{item}[$itemno-1]);
	$disp.=$ITEM[$itemno]->{name}."�͑q�ɂɂ����ς��Ȃ̂Ő������Ƃ��߂܂����B<br>" , next if !$count;

	$flag++;
	$DT->{item}[$itemno-1]+=$count;
	$DT->{_lord}->{"stock$i"}-=$count * $MYMANOR[5];
	my $ret=$ITEM[$itemno]->{name}."��".$count.$ITEM[$itemno]->{scale}."����";
	$disp.=$ret."���܂����B<br>";
	PushLog(0,$DT->{id},"�����ɂ�".$ret);
	}

if ($flag)
	{
	WriteDTSub($DT,"lord");
	RenewLog();
	DataWrite();
	DataCommitOrAbort();
	}
	else
	{
	$disp.='�����\�Ȃ��̂�����܂���ł����B';
	}
UnLock();
OutSkin();
exit;
}





