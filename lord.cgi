# �̎�@ 2005/01/06 �R��

DataRead();
CheckUserPass(1);
ReadArmy();

$disp.="<BIG>���̎���</BIG><br><br>";

# �v�Z����
my %msg; $msg{free}=""; $msg{double}="";
foreach my $DT (@DT)
	{
	$msg{free}.=$DT->{shopname}."�C " , next if ($DT->{taxmode}==1);
	$msg{double}.=$DT->{shopname}."�C " if ($DT->{taxmode}==2);
	}

$msg{free} = substr($msg{free},0,(length($msg{free})-3)) if ($msg{free});
$msg{double} = substr($msg{double},0,(length($msg{double})-3)) if ($msg{double});


if (defined($id2idx{$STATE->{leader}}))
{
my $i=$id2idx{$STATE->{leader}};
$disp.=$TB.$TR.$TD.GetTagImgKao($DT[$i]->{name},$DT[$i]->{icon});
$disp.=$TD."<SPAN>�̎�</SPAN> �F <b>".$DT[$i]->{name}."</b>";
$disp.=DignityDefine($DT[$i]->{dignity})." <small>�i".$DT[$i]->{shopname}."�j</small><br>";
$disp.=">> ".$DT[$i]->{comment};
$disp.=$TRE.$TBE;
}
else
{
$disp.=$TB.$TR.$TD.GetTagImgKao($BAL_NAME,"bal");
$disp.=$TD."�̎� �F <b>$BAL_NAME</b> <small>�i$BAL_JOB�j</small><br>";
$disp.=">> ���̊X�̓I���̕����B������͂��́I";
$disp.=$TRE.$TBE;
}

my $armycost=200-int($STATE->{safety} / 100); 	# 100 - 200
my $purpose="�����d��";
if ($DTTaxrate < 20) { $purpose="�l�����"; }
elsif ($STATE->{army}*$armycost*2 > $STATE->{devem}+$STATE->{safem}) { $purpose="�R���d��"; }

$updown="(�����W)";
my $peopleud=(24000 * $DTusercount) + 100000 + ($STATE->{develop} * 30) + ($STATE->{safety} * 20);
if ($DTpeople > $peopleud + 10000) { $updown="(������)"; }
elsif ($DTpeople > $peopleud - 10000) { $updown="(�����)"; }

$disp.="<br><BIG>��������</BIG><br><br>";
$disp.="<table width=480>".$TR;
$disp.=$TDB."�l��".$TD.int($DTpeople/10)."�l <small>".$updown."</small>";
$disp.=$TDB."���j".$TD.$purpose.$TRE;
$disp.=$TR.$TDB."�X����".$TD.GetMoneyString($STATE->{money}+0);
$disp.=$TDB."�ŗ�".$TDNW.GetTaxMessage($DTTaxrate+0).$TRE;
$disp.=$TR.$TDB."�O���Ŏ�".$TD.GetMoneyString($STATE->{in}+0);
$disp.=$TDB."�O���Ώo".$TD.GetMoneyString($STATE->{out}+0).$TRE;
$disp.=$TR.$TDB."�J��".$TDNW.GetRankMessage($STATE->{develop}+0) ;
$disp.=$TDB."�J��΍���".$TD.GetMoneyString($STATE->{devem}+0).$TRE;
$disp.=$TR.$TDB."����".$TDNW.GetRankMessage($STATE->{safety}+0) ;
$disp.=$TDB."�����΍���".$TD.GetMoneyString($STATE->{safem}+0).$TRE;
$disp.=$TR.$TDB."�ƐœX<td colspan=3><small>".$msg{free}."</small>".$TRE;
$disp.=$TR.$TDB."�{�œX<td colspan=3><small>".$msg{double}."</small>".$TRE;
$disp.=$TBE;

$disp.="<br><BIG>���R����</BIG><br><br>";
$disp.=$TB.$TR;
$disp.=$TDB."��q�R".$TD.GetArmyMessage($STATE->{army}+$STATE->{robina}+0,"b");
$disp.=$TDB."���͈ێ���".$TD.GetMoneyString($STATE->{army}*$armycost).$TRE;

if ($DTevent{rebel})
{
foreach(keys(%RIOT))
	{
	next if !defined($id2idx{$_});
	$STATE->{rebel}+=$ARMY{$_};
	$DT[$id2idx{$_}]->{army}=$ARMY{$_};
	}
$STATE->{rebel}+=$STATE->{robinb};
@DTS=sort{$b->{army}<=>$a->{army}}@DT;
my $rebelid=$DTS[0]->{id};
$rebelid=$DTS[1]->{id} if ($rebelid == $STATE->{leader});
$disp.=$TR.$TDB."�����R".$TD.GetArmyMessage($STATE->{rebel},"r");
$disp.=$TDB."���".$TD."<SPAN>����</SPAN>".$TRE;
	if ($STATE->{robinb} > $DT[$id2idx{$rebelid}]->{army})
	{
	$disp.=$TR.$TD.GetTagImgKao($BAL_NAME,"bal");
	$disp.="<td colspan=3><SPAN>�������[�_�[</SPAN> �F <b>$BAL_NAME</b> <small>�i$BAL_JOB�j</small><br>";
	$disp.=">> �̎�̎㕺�ȂǑ���ɂȂ�񂼁I������͂��́I";
	}
	else
	{
	$disp.=$TR.$TD.GetTagImgKao($DT[$id2idx{$rebelid}]->{name},$DT[$id2idx{$rebelid}]->{icon});
	$disp.="<td colspan=3><SPAN>�������[�_�[</SPAN> �F <b>".$DT[$id2idx{$rebelid}]->{name}."</b>";
	$disp.=DignityDefine($DT[$id2idx{$rebelid}]->{dignity})." <small>�i".$DT[$id2idx{$rebelid}]->{shopname}."�j</small><br>";
	$disp.=">> ".$DT[$id2idx{$rebelid}]->{comment};
	}
	$disp.=$TRE;
}
else
{
$disp.=$TR.$TDB."�����R".$TD."�s��";
$disp.=$TDB."���".$TD."����".$TRE;
}
$disp.=$TBE;

if (!$GUEST_USER && $STATE->{leader}==$DT->{id})
	{
	$disp.=<<STR;
	<br>
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="lord-f">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=form VALUE="plus">
	<INPUT TYPE=SUBMIT VALUE='����������s��'>
	</FORM>
STR
	}

OutSkin();
1;


sub GetTaxMessage
{
	my($per)=@_;
	
	return $per."%" if $MOBILE;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/r.gif" width="|.($per * 2).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100 - ($per * 2)).qq|" height="12">| if $per!=50;
	$bar.=" ".$per."%";
	$bar.="</nobr><br>";
	
	return $bar;
}

sub GetArmyMessage
{
	my($rank,$mode)=@_;
	return $rank."�l" if $MOBILE;
	my $per=int($rank/500);
	$per=100 if $per>100;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/$mode.gif" width="|.(    $per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=200;
	$bar.=" ".$rank."�l";
	$bar.="</nobr><br>";
	
	return $bar;
}
