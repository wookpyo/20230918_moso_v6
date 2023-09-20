from django import forms
from .models import (
    Injection,
)
from django.core.validators import RegexValidator


class InjectionForm(forms.ModelForm):


    male_1 = forms.CharField(
        label='작업 관리자', min_length=1, max_length=50, initial="", 
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    male_2 = forms.CharField(
        label='남성1', min_length=1, max_length=50, initial="", 
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )


    male_3 = forms.CharField(
        label='남성2', min_length=1, max_length=50, initial="", 
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    female_1 = forms.CharField(
        label='여성1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    female_2 = forms.CharField(
        label='여성2', min_length=1, max_length=50, 
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )


    female_3 = forms.CharField(
        label='여성3', min_length=1, max_length=50, 
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    female_4 = forms.CharField(
        label='여성4', min_length=1, max_length=50, 
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    female_5 = forms.CharField(
        label='여성5', min_length=1, max_length=50, 
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    female_6 = forms.CharField(
        label='여성6', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    female_6 = forms.CharField(
        label='여성6', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    product_name = forms.CharField(
        label='제품명', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    product_color = forms.CharField(
        label='제품 색상', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    order_quantity = forms.CharField(
        label='주문 수량', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    order_number = forms.CharField(
        label='주문 번호', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    quantity = forms.CharField(
        label='생산 수량', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    quantity_per_box = forms.CharField(
        label='박스 당 개입 수', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    box_quantity = forms.CharField(
        label='생산 박스 수', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    chiller_temperature = forms.CharField(
        label='칠러 온도', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    hopper_temperature = forms.CharField(
        label='호퍼 온도', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    hot_oil_temperature = forms.CharField(
        label='온유기 온도', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    masterbatch_dry_temperature = forms.CharField(
        label='MB 건조 온도', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    resin = forms.CharField(
        label='원료', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    masterbatch_number = forms.CharField(
        label='MB 번호', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    cycle_time = forms.CharField(
        label='싸이클 타임', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    cavity_weight = forms.CharField(
        label='캐비티 중량', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    cavity_quantity = forms.CharField(
        label='캐비티 수', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    time_injection1 = forms.CharField(
        label='타이머설정(사출) - 사출 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection2 = forms.CharField(
        label='타이머설정(사출) - 냉각 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection3 = forms.CharField(
        label='타이머설정(사출) - 사출 시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection4 = forms.CharField(
        label='타이머설정(사출) - 스크류 장전 시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection5 = forms.CharField(
        label='타이머설정(사출) - 스크류 감압 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection6 = forms.CharField(
        label='타이머설정(사출) - 핫 러너 차단 폐쇄', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection7 = forms.CharField(
        label='타이머설정(사출) - HR 밸브 주입구 핀 개방 시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection8 = forms.CharField(
        label='타이머설정(사출) - 차단 노즐 폐쇄 시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection9 = forms.CharField(
        label='타이머설정(사출) - 사출코어금형 에어 분사 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    time_injection10 = forms.CharField(
        label='타이머설정(가열) - 가열 코어 하강 시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection11 = forms.CharField(
        label='타이머설정(가열) - 가열 코어 하강 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection12 = forms.CharField(
        label='타이머설정(가열) - 가열 포트 상승 시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection13 = forms.CharField(
        label='타이머설정(가열) - 가열 포트 상승 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection14 = forms.CharField(
        label='타이머설정(가열) - 온조 블로우 시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection15 = forms.CharField(
        label='타이머설정(가열) - 온조 블로우 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection16 = forms.CharField(
        label='타이머설정(가열) - 온조 블로우 감압', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection17 = forms.CharField(
        label='타이머설정(가열) - 온조부냉각 블로 개시', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection18 = forms.CharField(
        label='타이머설정(가열) - 조건부 냉각 블로우 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection19 = forms.CharField(
        label='타이머설정(가열) - 조건부 냉각 블로우 감압 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    time_injection20 = forms.CharField(
        label='타이머설정(블로우) - 블로우 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection21 = forms.CharField(
        label='타이머설정(블로우) - 블로우 감압 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection22 = forms.CharField(
        label='타이머설정(블로우) - 1차 블로우 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection23 = forms.CharField(
        label='타이머설정(블로우) - 2차 블로우 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection24 = forms.CharField(
        label='타이머설정(블로우) - 블로우 에어 복구', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection25 = forms.CharField(
        label='타이머설정(블로우) - 냉각 블로우 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection26 = forms.CharField(
        label='타이머설정(블로우) - 스트레치 하강 시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection27 = forms.CharField(
        label='타이머설정(블로우) - 스트레치 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    time_injection28 = forms.CharField(
        label='타이머설정(블로우) - 보톰 금형(지연)시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    heating_setting1 = forms.CharField(
        label='온도설정(배럴) - 노즐', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting2 = forms.CharField(
        label='온도설정(배럴) - 전면', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting3 = forms.CharField(
        label='온도설정(배럴) - 가운데', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting4 = forms.CharField(
        label='온도설정(배럴) - 후면F', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting5 = forms.CharField(
        label='온도설정(배럴) - 후면R', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    heating_setting6 = forms.CharField(
        label='온도설정(HR노즐) - 1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting7 = forms.CharField(
        label='온도설정(HR노즐) - 2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting8 = forms.CharField(
        label='온도설정(HR노즐) - 3', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting9 = forms.CharField(
        label='온도설정(HR노즐) - 4', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting10 = forms.CharField(
        label='온도설정(HR노즐) - 5', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting11 = forms.CharField(
        label='온도설정(HR노즐) - 6', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting12 = forms.CharField(
        label='온도설정(HR노즐) - 7', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting13 = forms.CharField(
        label='온도설정(HR노즐) - 8', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting14 = forms.CharField(
        label='온도설정(HR노즐) - 9', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting15 = forms.CharField(
        label='온도설정(HR노즐) - 10', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting16 = forms.CharField(
        label='온도설정(HR노즐) - 11', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting17 = forms.CharField(
        label='온도설정(HR노즐) - 12', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    heating_setting18 = forms.CharField(
        label='온도설정(HR블록) - 1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting19 = forms.CharField(
        label='온도설정(HR블록) - 2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting20 = forms.CharField(
        label='온도설정(HR블록) - 3', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting21 = forms.CharField(
        label='온도설정(HR블록) - 4', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting22 = forms.CharField(
        label='온도설정(HR블록) - 5', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting23 = forms.CharField(
        label='온도설정(HR블록) - 6', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting24 = forms.CharField(
        label='온도설정(HR블록) - 7', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting25 = forms.CharField(
        label='온도설정(HR블록) - 8', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting26 = forms.CharField(
        label='온도설정(HR블록) - 스프루', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    heating_setting27 = forms.CharField(
        label='온도설정(가열 코어) - 1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting28 = forms.CharField(
        label='온도설정(가열 코어) - 2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting29 = forms.CharField(
        label='온도설정(가열 코어) - 3', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting30 = forms.CharField(
        label='온도설정(가열 코어) - 4', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting31 = forms.CharField(
        label='온도설정(가열 코어) - 5', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting32 = forms.CharField(
        label='온도설정(가열 코어) - 6', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting33 = forms.CharField(
        label='온도설정(가열 코어) - 7', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting34 = forms.CharField(
        label='온도설정(가열 코어) - 8', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting35 = forms.CharField(
        label='온도설정(가열 코어) - 9', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting36 = forms.CharField(
        label='온도설정(가열 코어) - 10', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting37 = forms.CharField(
        label='온도설정(가열 코어) - 11', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting38 = forms.CharField(
        label='온도설정(가열 코어) - 12', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    heating_setting39 = forms.CharField(
        label='온도설정(가열 포트 L) - 1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting40 = forms.CharField(
        label='온도설정(가열 포트 L) - 2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting41 = forms.CharField(
        label='온도설정(가열 포트 L) - 3', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting42 = forms.CharField(
        label='온도설정(가열 포트 L) - 4', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting43 = forms.CharField(
        label='온도설정(가열 포트 L) - 5', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting44 = forms.CharField(
        label='온도설정(가열 포트 L) - 6', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting45 = forms.CharField(
        label='온도설정(가열 포트 L) - 7', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting46 = forms.CharField(
        label='온도설정(가열 포트 L) - 8', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting47 = forms.CharField(
        label='온도설정(가열 포트 L) - 9', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting48 = forms.CharField(
        label='온도설정(가열 포트 L) - 10', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting49 = forms.CharField(
        label='온도설정(가열 포트 L) - 11', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting50 = forms.CharField(
        label='온도설정(가열 포트 L) - 12', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    heating_setting51 = forms.CharField(
        label='온도설정(가열 포트 R) - 1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting52 = forms.CharField(
        label='온도설정(가열 포트 R) - 2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting53 = forms.CharField(
        label='온도설정(가열 포트 R) - 3', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting54 = forms.CharField(
        label='온도설정(가열 포트 R) - 4', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting55 = forms.CharField(
        label='온도설정(가열 포트 R) - 5', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting56 = forms.CharField(
        label='온도설정(가열 포트 R) - 6', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting57 = forms.CharField(
        label='온도설정(가열 포트 R) - 7', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting58 = forms.CharField(
        label='온도설정(가열 포트 R) - 8', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting59 = forms.CharField(
        label='온도설정(가열 포트 R) - 9', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting60 = forms.CharField(
        label='온도설정(가열 포트 R) - 10', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting61 = forms.CharField(
        label='온도설정(가열 포트 R) - 11', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    heating_setting62 = forms.CharField(
        label='온도설정(가열 포트 R) - 12', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    injetion_setting1 = forms.CharField(
        label='사출 제어 (위치 mm) - M2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting2 = forms.CharField(
        label='사출 제어 (위치 mm) - M1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting3 = forms.CharField(
        label='사출 제어 (위치 mm) - P-V', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting4 = forms.CharField(
        label='사출 제어 (위치 mm) - 3-2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting5 = forms.CharField(
        label='사출 제어 (위치 mm) - 2-1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting6 = forms.CharField(
        label='사출 제어 (위치 mm) - 사출 크기', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting7 = forms.CharField(
        label='사출 제어 (압력 MPa) - 5', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting8 = forms.CharField(
        label='사출 제어 (압력 MPa) - 4', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting9 = forms.CharField(
        label='사출 제어 (압력 MPa) - 3', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting10 = forms.CharField(
        label='사출 제어 (압력 MPa) - 2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting11 = forms.CharField(
        label='사출 제어 (압력 MPa) - 1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting12 = forms.CharField(
        label='사출 제어 (속도 %) - 5', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting13 = forms.CharField(
        label='사출 제어 (속도 %) - 4', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting14 = forms.CharField(
        label='사출 제어 (속도 %) - 3', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting15 = forms.CharField(
        label='사출 제어 (속도 %) - 2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting16 = forms.CharField(
        label='사출 제어 (속도 %) - 1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting17 = forms.CharField(
        label='사출 제어 (사출 시간)', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting18 = forms.CharField(
        label='사출 제어 (냉각 시간)', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting19 = forms.CharField(
        label='사출 제어 (사출 시작)', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    injetion_setting20 = forms.CharField(
        label='스크류 회전 (흘림 방지 초)', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting21 = forms.CharField(
        label='스크류 회전 (위치 PN1)', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting22 = forms.CharField(
        label='스크류 회전 (사출 크기)', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting23 = forms.CharField(
        label='스크류 회전 (압력 MPa) - 흘림 방지', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting24 = forms.CharField(
        label='스크류 회전 (압력 MPa) - 1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting25 = forms.CharField(
        label='스크류 회전 (압력 MPa) - 2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting26 = forms.CharField(
        label='스크류 회전 (속도 %) - 흘림 방지', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting27 = forms.CharField(
        label='스크류 회전 (속도 %) - 1', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting28 = forms.CharField(
        label='스크류 회전 (속도 %) - 2', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting29 = forms.CharField(
        label='스크류 회전 - 스크류 감압 시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting30 = forms.CharField(
        label='스크류 회전 - 스크류 장전 시작', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting31 = forms.CharField(
        label='스크류 회전 - 스크류 속도 상승', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    injetion_setting32 = forms.CharField(
        label='퍼지 펌프 설정(스크류 후진) - 압력 MPa', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting33 = forms.CharField(
        label='퍼지 펌프 설정(스크류 후진) - 속도 %', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting34 = forms.CharField(
        label='퍼지 펌프 설정(사출장치 전진) - 압력 MPa', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting35 = forms.CharField(
        label='퍼지 펌프 설정(사출장치 전진) - 속도 %', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting36 = forms.CharField(
        label='퍼지 펌프 설정(사출장치 후진) - 압력 MPa', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting37 = forms.CharField(
        label='퍼지 펌프 설정(사출장치 후진) - 속도 %', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting38 = forms.CharField(
        label='퍼지 펌프 설정(언로드) - 압력 MPa', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting39 = forms.CharField(
        label='퍼지 펌프 설정(언로드) - 속도 %', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting40 = forms.CharField(
        label='퍼지 경보 설정(과보압)', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting41 = forms.CharField(
        label='퍼지 경보 설정(미성형)', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting42 = forms.CharField(
        label='퍼지 퍼지 설정(사출) - 압력 MPa', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting43 = forms.CharField(
        label='퍼지 퍼지 설정(사출) - 속도 %', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting44 = forms.CharField(
        label='퍼지 퍼지 설정(장전) - 압력 MPa', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting45 = forms.CharField(
        label='퍼지 퍼지 설정(장전) - 속도 %', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    injetion_setting46 = forms.CharField(
        label='퍼지 퍼지 설정(반복 횟수)', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )


    BOTTOM_OPTION = [('bottom_normal', 'bottom_normal'), ('bottom_top_fix', 'bottom_top_fix'), ('bottom_top_delay', 'bottom_top_delay')]
    bottom_option = forms.CharField(label='보톰 옵션', widget=forms.RadioSelect(choices=BOTTOM_OPTION))

    WORK_TEAM = [('주간', '주간'), ('야간', '야간')]
    work_team = forms.CharField(label='작업 시간', widget=forms.RadioSelect(choices=WORK_TEAM))

    work_time = forms.CharField(
        label='작업시간', min_length=1, max_length=50,
        validators=[RegexValidator(
        message="Only letters is allowed !")],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    message = forms.CharField(
        label='About you', min_length=5, max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Talk a little about you', 'rows':5}
        ),
    )

    class Meta:
        model = Injection
        # fields = ['user_name', 'user_number', 'quantity', 'message']
        fields = "__all__"


        widgets = {
            'work_date':forms.DateInput(
                attrs={
                    'style':'font-size: 17px; cursor: pointer',
                    'type':'date',
                    'onkeydown':'return false',
                }
            )
        }