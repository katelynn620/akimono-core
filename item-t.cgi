# �A�C�e���j�� 2005/01/06 �R��

$NOMENU=1;
$Q{er}='stock';
Lock();
DataRead();
CheckUserPass();

$itemno=CheckItemNo($Q{item});
$itemname=$ITEM[$itemno]->{name};
$scale=$ITEM[$itemno]->{scale};
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$DT->{item}[$itemno-1]);

if ($ITEM[$itemno]->{flag}=~/h/) {

OutError('�s���ȗv���ł�') if ($ITEM[$itemno]->{flag}=~/t/);
OutError('���ِl�����w�肵�Ă�������') if !$count;

$ret=$itemname."��".$count.$scale."���ق��܂���";
$disp.=$ret;
$DT->{item}[$itemno-1]-=$count;

 }	else	{

OutError('�s���ȗv���ł�') if ($ITEM[$itemno]->{flag}=~/t/);
OutError('�j�����ʂ��w�肵�Ă�������') if !$count;

$ret=$itemname."��".$count.$scale."�������܂���";
$disp.=$ret;
$DT->{item}[$itemno-1]-=$count;
$DT->{trush}+=int($ITEM[$itemno]->{price} * $count / 5);	#����

$DTwholestore[$itemno-1]+=$count;
my $limit=0;
foreach $DT (@DT)
	{$limit+=$DT->{item}[$itemno-1];}

my $ITEM=$ITEM[$itemno];
my $limitcount=$ITEM->{wslimit}<0 ? -$ITEM->{wslimit} : int($ITEM->{wslimit}*($#DT+1));

if($limit+$DTwholestore[$itemno-1]>$limitcount)
{
	$limit=$limitcount if $limitcount<$limit;
	$DTwholestore[$itemno-1]=$limitcount-$limit;
}
$DTwholestore[$itemno-1]=0 if $DTwholestore[$itemno-1]<0;

	if ( $DT->{guild} && $ITEM[$itemno]->{price}) {
	ReadGuild();
	ReadGuildData();
	if ( $GUILD_DATA{$DT->{guild}}->{money} <= 0 ) {
		$disp.="<br>�M���h����̕⏕���͂���܂���ł���";
		} else {
		my $guildmargin = int( $ITEM[$itemno]->{price} * $GUILD{$DT->{guild}}->[$GUILDIDX_dealrate] * $count / 1000 );
		$guildmargin = $GUILD_DATA{$DT->{guild}}->{money} if ($guildmargin > $GUILD_DATA{$DT->{guild}}->{money});
		$disp.="<br>�M���h����".GetMoneyString($guildmargin)."�̕⏕�����x������܂���";
		$ret.="/�M���h����".GetMoneyString($guildmargin)."�x��";
		EditGuildMoney($DT->{guild} ,-$guildmargin);
		$DT->{money}+=$guildmargin;
		WriteGuildData() ;
		}
	}
}

PushLog(0,$DT->{id},$ret);
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;
