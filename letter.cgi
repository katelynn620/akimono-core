# �X�� 2004/01/20 �R��

$Q{mode}='new',  if ($Q{form} eq "make")&&($Q{ok}); 	# ���M���[�h�ؑ�
CoLock() if $Q{mode};

$NOITEM=1;
DataRead();
CheckUserPass();

$image[0]=GetTagImgKao("����`��","help");
$WriteFlag=0;						# �X�V�t���O�B

ReadLetterName();
ReadLetter();

RequireFile('inc-letter-edit.cgi') if ($Q{mode});	# �e�폈��

if ($Q{form})
{
RequireFile('inc-letter-form.cgi');
}
else
{
RequireFile('inc-letter.cgi');
}

	if ($WriteFlag)
	{
	CoLock() if !$COLOCKED;
	WriteLetter();
	CoDataCA();
	CoUnLock();
	}
OutSkin();
1;
