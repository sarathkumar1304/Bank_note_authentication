import streamlit as st
import numpy as np
import pandas as pd
import pickle
from flask import Flask,request
from streamlit_option_menu import option_menu
pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def predict(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home",  "Project", "About Me"],
        icons=["house",  "app-indicator", "person-video3"],
        menu_icon="cast",
        default_index=0,
    )
if selected=="Home":
    st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoGCBUVExcTFRUYGBcYGyMaGhkaGxodHx0aIRwfHx8aIyMjIysjIyAoHR0fJTUmKCwuMjQyHCE3PDcxOysxMi4BCwsLDw4PHRERHTEpIykxMTE5MTMxMTExMzExMTExMTk0MzExMTExMTExMTExMTExMTExMTExMTExMTExMTExMf/AABEIAKIBNwMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAEBQADBgECB//EAEMQAAECBAQEAwUGBAQGAgMAAAECEQADITEEBRJBIlFhcQYTgTJCkaGxFCNSwdHwYnKy4TOCkvEVJDRDosIHUxaz0v/EABoBAAMBAQEBAAAAAAAAAAAAAAIDBAEFAAb/xAAwEQACAQMDAQgBAgcBAAAAAAABAgADESEEEjFBEyIyUWFxgZEzFEIFI1KhsdHxNP/aAAwDAQACEQMRAD8AbZSZcx5pCV20pCisIWHClArGpKy4BoPZG7mDtPSM9jFjUlcl0LDAr3UGI0kCiyCkixADnaCsuzoqUETQEkvpWn2S1xzBau4Z7QqrpnXIyICVkbHWMfIJcC37tHESwzM2x/WDELDAhiDUNY/lCTHZ/hk65ZmEk0JlhRajOFCj9jA0t4N1huFI70X5vmqioYWXxTVHSSLgbpfZTO52Fb2G/wDj9YTiJksf/X80qH6wTkWHwyDqkzPMWSQoqosJL0Zge5ap+ELcsX9nxqlKdgpQbcoVUH0ofQiOmDuUt/b1kIQlwoH/ACfRpc0AFywG5LUjk4xls6zgTgMPIdaphAJYil2DsbipsAD6O5coSJCJY4ilLDbUq57B/gIjdbS5Vso3SvHZ6nDAFfECfZF23I/dfmGE1EnGyAUqdJqlSbpU24NjWoMfNc2WuZMKpl7Ny6CPGVZjNkTNcpVxxJIOlQD0UNy1XDX2rCRUzniMbTBksc3+p9Ewnh9lPNmGaORFxsCSS46Q4UrYQp8O5/KxSeF0zAONBuOoPvDqPUCGa4cpB4k1PTrRuFFryAQJmpoB1c+n7+UFqWw/QPC3MpnH6CF1T3ZTSF2lCUEuBz+X+8VKUEpc/wCUfnAOaYqZLKZcv213VcJSG1MlxqUx9kF2c7AGYPFiYVaiCUK0q0klOoM4BYOHo/MEXBjmntF3FuOktUAmFSeZ3qYsWsCp9O8eVqAFbC5/KKA6jqP+WJY+14Ukbm/0jN+JsWk/cAtqrq5KBonkX32Nvehpi8d5aS6mIDlX4U8+52HrYGM1g8IvFrJP3coKdRZlEM2l9yaEm9t4r01Eu0nrVRTW5jDwHg/8ScCQknShLuBpPGRWo1Bgb8Jh3JxSJhUUqCmPtO2kAVcGrXPIvAmZ4lEmQJaRpB4EhPup3Pw35kQsTJCuIOpRUyFIcKl7gGgIpsWvu8dkns7IBk/U4ZPaksTiPZ6taUmYpCZStR1AtpSASQrUGDJ97YiExkKmztYCVS3uhRXoZ9TTAEKlqoj7shQOp+Zj35q0iYCAsUeahI1gg6gVJpqqA7M9YbZNO165xUhalhKDocABOq4JKtTqLvsANniRlZCWtkylNrACe/LLUA7G39opVL5UPI/kfy6QegRxcsEj9/uwhCuy8ExxRTyIAjUb0H7vvt9I5LDUcg8tm5jpXv6NB65LM1jt+/3WEvimd5cotRauFHN91dwH+I5xdR1BY7W69f8AcmqUQBdZn8ZnEzz1zZayAOFNaEJe43BLljz6U3+BxQUlK0nhWAodHEYeRl2rBKmlIC9WuzMhO3YglX+VPKHPgXEapSpRNZZp/Ka/Iv8AERS6krmTg2bE2BVu9I4O8Kc4xqpUrWltQUAAagjcXg7K8UZkpEwhioW9SPyeJttpWMruivxpmQk4cjXpXNPlpNKOOJVaBk2fcpjBYOfLSCJZSnmpwpTu19vT4wyz/OZc7ELctLlky0m6Sx4ybiqnuDQCPEjLAkFcoIBUOqkEitCOJHpqHMVgWOZ6eJOFWTqH3dySfaNKEA0bd1ULND/J8sfUpY8tNOIqBUsM7k+63IUEZtOMWgGTiEmXrHDMTUdC49obO5PPp3CZdMSykGWpJspKkkG1t7mCRukFhNac5kS0ESQC1CWIAPV6n6fSM9meazJhIcrvQUA/IetfrAK8MrzGJCn9pKFEN3U1L/pu16UJCeIpKR7qS0sd9ybVNLHlGs/QTLR5kWIUcPLPtMkJJDlynhO3MGJA3hyfqlqAdkLUB7t2U+1HUbRI51TUENadmlQVkBheFZctXGNLaiQxSXDVIcBgGcgEcoHxsjRpKUkMyuK9SWJ7gq5ewYX4STNlTFaVqS4ahCtQaiikbN6jaDp+NDaVaUrU2mW7qJYiifaAate3SO+52gnpPmU72Os9ZtiJv2BOgkDUUrYf9sKWAO1Eg9OjxX4YThJktMtUtJm11avaV1SeTbBiPmdTgcGESko5Jq9nNT8yYRZp4TlrJVLV5Re10+m6fSnSOajq3d4zzOgyMM8xdnHhpSD5sgqISX0++nmUndhsa94Z5NoxaCJyApcthrDpUQXaobkXFrUiuTgscB5f2hJDVLuWNKEp1fPlBctUrAyakqWrYAalmwAGwruWD3rFQJVO8YB2i4XxG3EMw2Fk4dtKQkrIQC5KlEmiaub7ClH2hlipXCHqYzGXy1T5iMQsAsoaXPCgBVkjcuPboSRswA2OKTSFB995roVGTmZHOMqC+IUVz/XnGOnYlKZipSuFSSQDsW3fb1+MfTZ6I+c+MMIZOJE7S6Fl/VtKkvzavr0iZlF4NPUOmOnlOiTMlkTEqKVg6gUmoPf9vG58J+J0zwJUxkzdj7q+3JX8Pw5D55NzKXLTwr1pNkC47PbsYNMsLAWjodwQeouDC0dk54nRUpXXGD5T6ytI3hRmS2UfxKHDR2pci7CFHhfxISRKxKmIoiYSK7Mrr/FvvzL3FIdRWEuWsd2t2hrurLiAlNkbMRqkGUkLLqUpQd+ImvEoafaLOQQHALQlxMiZKloIKtEtLIPl6ShNjMUCeOaUkhIYAkqPbW4dehQUoFRJZLg6nLaiAbBqXakKMylPNToUJi5iSVBQZJFON68IIGlLUe8SuxEpXJleAxomMiYUhafaQCHd+QJ2IJDltQEFY3EaQ7cRokbdz0Fyf1EK5SGEs8Ily1qUkAHWpZK0lPJ3UriB4r0Dwn8SZqQTLBdaqKI2H4AeQBqer7iELR3PiNL2EJ8teLmiUjWZQU8yYA7q/EdtmA2psK6U4CZ5QlypaZYDaVFjzel7gb11PeM5gfESpaEypEuWlI/EVLUqrPTSNR/fKLf/AMtm2IPoUCn+gn5x2KOymthOdV09Sq1zYCczAT0TEmejQlNpiAZiG6htQct0YCsEyZ8tQMxBEsA6UFJ1JNSTazs+w5gsYvyvMTiAp/NSE0IK1EFxycBwOYjOZ/lBRNVNkKUhaQmiA+pV3Iq9FC/KGNqAOYs/w4qtwZpZ4YhMwFPFqK0M6iSb0Yuej8ktElYUrUqaDoLsmZL5BwAofNq32jIYbPsRJ1ImICtR41JbYkHhPfZr2tDfLc4lzFKVLXUgsg3vRBB25PQNRoaGSoJI9KpTORHeFzwpJRNTVJ0lSRQlgbVO4dujO9HGGmpWnWlQULAg8uv5GvaM/PQAknh3cMl0nVUqYmuk+78xA2CmqlnUl0BdCeSrBVbgszdBaJqmlXlYaag8NNbMG0Ic4zfCr+7mAzQHB0h2NLFxXqmCM9xf/KKmJopTJI5Eq0qHOlQD2MKfD+QypkkTF6iVEggKbS1h3IY15iEJTUDcbxzOb7Vh2EzGStQTLUCCG8tVDQWD3o4vvCQYdeFnakEs/C9QU/gV1FiKGxpRrs28MrRxSz5gf2TRX6HfkehrBeQ5kTpkzgFpPCCupB/CXvXnUfS5GUpYGJRSrFiJRjcbMxK0SwAK0SHqWuTyA+AJjU5tOEjDBCFcRAlpO9qq6FnPciLMLg0Ify0JD3YAH4/lCPPFKmL1o4gigRTiHvEbantsWA6pBxDFTdhRYRZ/whC0lTaSB7Qoac+fq4gfDYGdLJXLJUn+EEgX9tP5jlGtyyWlUsKSygaj97F9otmoDlZofq27et4VTUNcTzNaZX/isuYky5iAl7lQ1S1Hn0L+tBUWgA5QJatSNRS3sat+aVUfkASDUsTvr14CTMdZlpUoggvuH+tL/rHrCZPKTLMtLhLk9Q/u9uhh4phRFFiZkcPjSsFKZWkJJSQpkhJZ6jt3P5W4XLVrJMtAmK3UoMhJ7H/2L1NIc5p4bKkEJVrLMWJQWewU/wD4mnaHuWSFIkoQptSUgHSGFOgoITVpta68xiEXsYiyvL1SlqC1aipCVdAQ4IB6U/tEhrj0NNlq56kfEav/AFiRyXuTO1QbuCZyVhkKBOtSkUSEqUpJJfkGpbn7QdoMyaYmQCkykg21pAertqIqRq4bx6lDQrTpUVrTVJZwpV9LVL09p9+sXIkpKwkBxrSCDQsFpZxtY0jto5LWORIKlFAmAAYdl85S6MHAc8z15fvrBE9ZFx2p/ePeMxyUUSxUKdB0/sIy+bZ2vWZUvjnK5+yhxQq68k/rX1SggPaNgeUgWsx7iZP+IyzLNtBEqWAuaqoSbJH419OQFT0uEeayvvBLK9S6KmzFcy9TsEIS5YMA4hLlU2bhcSfNJUpagZhNdQPvjsLWs0bJGVkqVM1CYvVq0kMkqozmtmDbUBZ2bmajU7qgJ8PQTp6fThEx4upg8xZ0JCQUSkhkJsuYwo+4DB+ZF2Dvt59jHz/NMPMUNa9RS7TEpTsxIsX0u1AD3JEFYvxRNUtKEqRLlqbjSAtTPUgl02f3djD6NVQDF16TNa008xMIPEmIkJQUTVyw59lak19DeA8bhFTlFCJsyY1FLUtQl29gAcBUXuE/2vwWS4Mo8nyUoIqQoATHoHSr3gTuKbdALMGk36QnkzMSp+F1/dS9arjRL+YUph847jFzUDWmUUkU4lB+zAKB332jS4LJxIWrj1JIoDQgO5frQW+TCK88yyZN0hCXDVqkF3r8B8wecAQtsy2lokUBiTf3mYw+OTMZKwJcw2rwmtGOx6HmGeNH4fz4yiJM4vLslZujof4eu3ayNfhmeqaFTJRSkmtUnYMKHa3YR5x6lSlKEyWrywoJQkhlNbUHuDetKEOIEqP2yvkZn0mahKvdCnHdxeE+MkukJdVA8whxoNOEcq0YUI9IW+GczMv7tStUqwO8s8juE/TtB/iuQDL8zUxl8V2+HJfI72LgmBPexAsVMzGe4wI9nbglpGymsOln5FnuQFeDwwLKUDqu4CzTYAaXYKCiSHq73hhhMqVMUVrVpNkpSAAlPIXvc9dywh1lOUFSiEpQqg1FYS3c8J3KiA3vGHIoUWvPXt3jEaMKhNVcNmJOlmH8WmOrwyGpM25hQs1w+/12jU//AIzMFlS7vTWij/wadqQuzPLVy1pSaqWwQNSlb1cklg5368oIGGHUwnw1hwiSSDq1LJfsw5baSO79YzOc4qZOnTE+zLTMIetSDpcc7UHaNlJT5Up1gDQCpVmcB1C37frGbweEl0LLmrYeyGHU6nJd9nTBNDPSdwUsgGYvUJaQwQTwuzJlt7xFVE7UvFWC8MInKKlBlHkwYmoNAwIAelKwRMW5Zwop9iUhvLRWjm17dW3AManIMKqXLBXxLU6lG3Erp0DD09IS5IGJm0NzMjNweKw5ofOlpppUSCOoVdwa1e0WJziXN4FjyplilQCdXR7GoepfbqdhMQ5qLfv994AzDKpUyWoFKSpRYDdh+/nB0tU4NjJq2jRhjEGykCbLmyFiiwFPShs9eRSktCcLn4Sa1ifVKwN/2xD9TD7J/B8yS8yXOUmjJlqGpIFL7i1kkflBOJWtKSjESuH8QdaDyNnSepFOcMNQqcjB6SBqQ4ByOsHwGfylsJjy1W3UPQgOLbj1MLM6UibiECTcgJJAup6H0G/TpQ+XkMhfHLWpINgCFJ9Dc/E2g3J8slyzqTxKtqJBbs1Gimmq+JesWX2jvc5hmPmKSghPtKoOg3Pz+JELsJgVu7OfSGOD41Ffu+725+tT6iGYWAP9oQdVT3EXm06TBeIFh8B5TrT71VIFn/EnrzG7c7+Mbh/MAYhruz9iC8C5nnGt5co1IobvvSnJzavIuEqVZHnPlrMtZOjcn3CTdVaJJ6nnUOorNUBty4jOzJxHOHwrJYkvW1hX5f3iwlr/ABi3Mpply1LCCvSH0puf7ftjCnB4pOKkLCTpUUlKh+EkM45j93ilKpbmIZbcQTG+KJSFMh5lbhtPoT+VIOyjP5c06QSleyVC/ZiQfi/SEHhtCZc9UuYkBbMkLahewfmGY7+sF+Ict1gTJSSmaFC1Ca3/AJhd7t6M5bkXgkgR5nZJlFQuCCOd2+hiR5wSJipYM3TqYO1ifh62iQl6KE3tKErMBaJDMmhISmUoB3GpQSxs9gfQUjuHlTAylrHRKAWHqam/QdId4iWk8ST6cv1hFnK5n+FJDrpqVfy0ksD/ADchtc9bgtOku4yJq9asdgPMXZ/mpCvs8gpM8jcgaX+RWRYep6pskXOwxOuUpeoudQLqJqSFC786xbnPh1MgIVrKlTHKtVS4Zz1BfeNllC5hkSn4lFIKldCN/Tl8rHk6ysaguePKdTSadaWBz5xBhsJMxU8T5yRLQkAJBcOA5CQLkOXJ3dh01mS4SZNUFuUSklw1Co7/AL/YIlyEHSmYH10Ske0prkVNA9y14H8U+JUYMCTKAmT1UShuFANnA9GSKm/KJ6GkaswLD4lFXULTUgc+cZZngikPUpHvD2k/qPlzEZbNMnSTqDIUfebgWTzHuqPzpU2jUeGPEUvFJAYy5rajLVuPxJPvJ+m/X1meWkPMlB39qXsr+V6P0sfqVXSNSYlfr/UXS1CuLN9zCYbFzcOoy1ClXlqqCNyDuP2btD/DYqXiA11CoQSykfxJUGL+vSgeOTsOiYnSBqTug0Ukj8JNQQfdPoRaEszL1JmJCFFQKgARRaKtxAszfFnteFq4PvGlLTTISwGtZU11KYUenS1I9TMWSvhTwi5Nz2/fwhD4sx60mXIlkhS7kM4DsAOTnfZorneFJjAmakqsaqLHrvX8o1T59ZUQosJp14pKrv8AKMt4hQDiBy1S9+n+94pmZTi5I1omEgVISomnPSQx+cdVPOIk+aQNSDpXy5pX0dyDy22hiqBBKgcQZOHIRMKXSpK7pYMnzHPppNQaVaBsfiJihLTMWNEpT6QGDguCeZ02Fg/wZS515gdXuzUEejkDnY0+JDEedhARqQdaCOWo6atqAqptlBz83IgQR6xngpiFIBCgaUb6fGG2WYoyiXSSFM+xpY/M/GMdgcKApemhZmBBHEQk0OlQ4VE32PWDEJYDiUk1YPQb+8nkb6jA2mMt5tVZxLF0rHoD+cJZ89M/HSylyJaCahrA/nNHw6QlVMWBSYS38hf4KffltB/h0KE/XqJOk6nYuGDdRxEWu3pA2tmCqWjPN0EoWEs6uEGm5rty+kIcXLlyuGdOUom6HKiB2ADW3I2h1n+L8qXrvpdQHM+yB2dQhB4UwAnLVNmjVpO+6zUk9rt/FBhyReUECNMixWGUoJlniuARprdwG0v8TD4qIqDGL8VSgjEJ8oBKwlJp+Ny3qzQf42xhTolIUUlyolJILVSP/J/gIEjM8CJpZJWo6QhyflzJhvgsCmXxXXz5dv1vAPhSYfIQlb+ZpBUVFyXq7/KG8NRB4uTOfqKzElRgTkedINDHowpz3OEyRpDKmGw5Dmf0jztbmTATzmOTSlOtJMpe60HT8dj6wvwWEmklBmS5iG9tJZTbggOLbho8YbLZuI+8nLKUmw3boLJH9+kTNcoRJR5kta0qTZyK1ajAMaj5CJDVYEhWteM7JWsWHEeBKUJqwA3hTmk4qKNVJRLFIUAojmaFx0BBtXl5wuYKXLE1QK1CyQwqPeHN6F9thCjEYnzFUHGosGcjs3x4mduYpG0qKgXM1mPAgpUnUsBySnhYixKVMGT+AEMO0XaQUHiCSU1diQbOoUJ2sCQLiwjuNQlIYq+9DnWBRG7dTUl9iSRWwqMFPKVkIQokbhV9STVgCS1d9rvHnCtzMQlTiN/DmOVKKcPNJKDSTMURXkhxSoqkAqYMkl2Ees5yKYmZ5+GBBVRSU0IfcdCbjY1tZFh5hD+cELS2hMpIYDUXcGhALF2DFnvG08M5ipafKmHivLVupDOAqlFgf6gNQ3aihVF9sGpSIzFGXeEffnKcmpSDf+ZX6fGNJ9hDANbr+zBpEcaK95ETtEGl4QDlEgpokZuabYTG/bFJVoQNcwnSjkTupW+kCpNOW8PsnywS0EHiUqq1G6ibvFWRZWUEzZgHmru1kJ2QnoNzuaw1xeKTLHM7D8zyEbUq3F2mUqIBsomEzXw/MXi1KmqBlgjRYak3CejEMSaluTNpMNhdOngJchIASeVzQaQztW8WoUpa2PFMIJCS5SmgPGQSAC7AEOfSGWCwgluX1LU2pZCQVNZ2AFBakSrT3m546CVs+0WHPnKEo0ghSiFqSypiQ1gQCAXDjqKsH2EfLfE2QTMMpapiytMwumdxHXclK78RLGtCzg3b69PQCkhVoFXh9aTLmJC5agxCgC4rcWG1uQtF9KoaftI6ib58l8O5fNnzkS8OWMslSpocBDltTu9k0FCSTShI+yYdBCUpUoqIABUQAVFqqYUD3pA+U5bLw8sSpSAlIrzJPMk1J6nkOUFx6tV3n0nqdPaIn8RZCmekqQfLmtwzA/tbEtdmHpQuKQnCFec0xBQpIc1BfYPT1BF2vSNRjcfLlsFmp2FS3M9I7icOiakV6pUGP+4iCrSDeHmXUqhW24YmE8RZQqbMC0KZaQGelLioqCC7d4GTj8dL4VS9bb6NX9BgDMcpxErE+UtWlSySlbqCVk7gjcnbYkc3gk4LHJA0kqb+MGl/fhIBTBIl+4MLiEzM1xkwFAlaXDOELDeqiwhhkGViVKKFEEqLqaos2ken1MJ/tmPRQy1H/Ikj/wAfzjTKmaQAQX3pvBMcYmrzFU7I1hfmSlAUo7gtyNGIsH/sw/8AwqYS5ToU76pakMeZY27itI0utLAPHUztqQt6hGJm0GZqZh8QKFKlAkE6UvuQ25ZiK9BFCFzUe6sc9QVyd/lGoxcwBClPppQgOxsGG5fbcwowc1YSpYUpLJ0njmq1KKhvMSAFgBQYPVVbCNWoT0gFYr+06vaZQfc/35Q28OhKlLUkMQyT1cv1/CPiINAW2pWrQrTp1lCixBsbE2oSTygjASWdkgOdgA/UtR6R5nGwzwXN4h8ZoUZZABISxLDkS7fI+kV5JnGHlYcJKuNJOpLFy5o21Q29OghvNmTdS1JShSXYJLpNKe1UGz+zAEzASSrVMwxSdyEhYJ/yuo+qY8FbaDbHpPdtTJtusYoyWSufiDiVBkhWp+avdAeh00+HWPErTiMVqJ4CoV28tO55PpD/AM0abypS0GVLmBJUNIAYKDjZNCIXSPB4B4ppIH4UgH5kt87wO7JLYh7l6TRpmBQC5Sw4fSoMRyIPMUqPoWMNsFiwuihpWKlP5g7j9mF2TZGJSNKXCXfiLklgOwt07Q3EhLaW/V+feG0EcX8vWQ6h6Z954xK9KSq7An4B4yXhzD+dNXOmcWkuxsVGo9ANv5RtGrKinhVXkdj0PX6/IZzE5ROlLK8MsMr3S1N2rQi9b1hFQtchsRaqORHuLxIQCSfjt1MZLMseqesIRUfX9Et+pvT1My7ETT98sAcnB9WTT6fKPONnowyfLl1mG6jUjf8AuB2ifeqmwyY2xI9IyQuXKQlClAEfEl7870+HKAMZPlkKMo6FqupjUcgRZy1r7xTgssUvjmE12ep7n9+kMJ2GlaFApAYGrVtzv++8atZd20nMw0za4mcVN0nSoOdgLgm2nmbdDtsqHGUZTRfmLAdLAMKJJCmPcpcpBZxvc+MplpOpary2KVcnenY/mo7wPmWaTNZQoBIL0UNQU3P02oRS1IeHG7baCEut7zznyB5adKA6a0KgHGoaqM7OnrvYQVhpayfNQltQCkq1VBKgpr0az7cj7J9YagC5hNUkiUWdQ/Ef4N7PTkHL3BZagyETNYQnSCwTQDkGMGVYmyCahQ+MwrB5skp+8ISsULOQXLBQpY8jUV7m05pJ/Hz2VsWO2xhVOwUou08UCgpkKokM5vsdNescVladTGaHoSnSr3k1HZhq9IcHrgeETez0/wDUYXmueiWAZUtU5btpSUoA7lbbbAH84kAnApCQrz0WcKLs4Ogqvu7R2C7St/SJ7sqHmYyzjNhK+7QNU00A2BNn5np1HR6sJKmEjUHm3UoglKLsWLEkkMySwrWkUZTl9yhXG/HNY7h+BwUqexUdj2h9h5SUJCEhkiwgkRmO5vryi3dVG1PuckSQgMl7vUkmpJuSTvFsR46IfETkSOEx0R6ekhdnOaCUNIrMIoNgOZ/SOTM7lCd5Gp1sbM2oe73Zz6c4qxyxNGhSQBsaageYhNV7CwOY+kg3AsMRZl+XTJ5VMUth+I1JU1m5Cn0HTuCzBWFWZcz2bkPZ/eT0PL6F4UZViymaAFO6tCqmtWFO9X784fY9MpgqaxALpfn03PaJlNhcYMvfnacg8WjPGS5c9CdQC00UlxY7KHX/AGhdiEmWeKo2IBr6c+kUo8RS3bSsjmw/WGsmbLnIcF0/MH8jGORU94tEamMjET/atT0oaAUd+f5eggbGApUkOdoKxGEEtTKc6i4VXm7OLdoozRBW2mh2N/jvCLEHMoRx0lgngqCSWHO7en7vFq0pIotBp2/vGfwxmkksrSpTFQFCRSnIbP6QzS591i9ocFuLkTzWHBkzdCfLZQJBoQCgWDn/ABOFu8BYDClKdKUB9bgHykskADiMshIOoqA0g0oQ7w8xMhMxGlcsm/EOFid+E8gHiiRliKBIWCOSlO7lTl3c6iTWCQk4Iii05NfSlIQQBZlLUwszi44QfhaC5RKUOTYOX7Wi/D5PQDUUgBmoSzafpBmYYdAlKpem+5Y/KC7AkWES1dVirDIZCQbxdpj1pjilN8f7/QRaihQAJymNySZXOlJKTqAI3cOI8ZVJ4XYoLnhClMGLWLDazNFuIVwE7MaHsaH1izLUtLTwhN6JoBU2gbAtDBIGIzk+Y1VJV3DH4inyi4LO6T6VH6/KPMuPZMehzh0qcUPMf2gObLKOqeZuO/Tr8ecJs2GMMxakHhfhS6CwFHZVHN4EwniKYlWia6KsTy/mCnYdmtaBq0BUWxhqSuQb+kd4hDxjsAjXi1+ZcEljuQbdWv6RqJs2YgupKVI30Agp66XLjmx7DaAM1ydE5pqFaVs4UmoPI/3j5urSfSuy1ODwZbTqLVUFenSXTVhIKlEAczCDH48zVeVKBYn/AFf2/wB+1ysgmKP3k1wO5p6mK5uNRJUZUlGpbsVGpJ5Bv9ukDQCA903P0BGMSecCOMrkCUjSak1J69O396Qvx+EMs60ALQCFMoOzcxyHO4c2vFSTjFVLJHJkD8ifjF8yRi0p9oc3LfpF2nViSdwPzEVdotgxJjcQXM0qJFyS+oF7kj3RQOOYDJcR9G8MTdeFkqvqQDZvlHzbESJqVFagG5inF2tZ4+keE2+ySWAA0BgLU27R0dOQSbSeqpCgmV4HHYafNmSkISpUsnW8sM7kGpFXL96x4zTN8HKUUzdIUCP+0pVgwsk7Fu0ZeXPm5fipzo1S5qnCiWCg5KWVzGogj+0NMDgRi55mzZYVLKS921FgAObAGLDYGchtW+4IvJJvjpHOVT8JiUHywhSUcJHllIDnUzKSLkP3iQh/+M5SkfaQpKhxpZwajiG8djxEupOxUGa1CAAwDDlHuIYkZGSARIhjytbBzQDeBJtNAnSaH6mAMVizUJoOe/pFWMnldBQOGB3rvA0xCnAUAOQv6t3/ADiSpWF9o5lNOlbJmW8RZQsL86WkuTqKQWU99SevS7/ICbnmIKPKK+K1EjXa3P4V6xs5ocsL77t8axJbu12se5c73jO0CjvRm0niZLK5H2cDETkkKH+FLNCotc8gPjbo/cBNm4qcyq81WCBsP0FzXqY54kUZmJ8v8OlCNmKgD9VfACNXgMEiSjQmgAcqO5Hvn90gXdbC45mruU4M8SsolJSxD0qon42oG/bwD4YxBTO0udKgXfpUE/veF3iHPBMBlyzwD2lW1NyP4X337XsySUsIMxRAURwgs+nbVycte1O0CxCgG1o5XJBUm95rsTNCqM46x5kyZarOOgO/r8YzszM1A+UhOpfN7A8+vT9nQZJhlJQNRc7vD0UnkSWo20YMJGBDM5bsIicvT3gkesWCHbB5RPaN5wWVhUDZzs5gmUA1Aw7N8oiEntHrTBAQGcnkzkUZkNQSkHd/QBvqRBQEDYpPGDyH1NfoIGq5VbiYADB04RW5DRRi8EsoICkgnfl1tsIZy1UjzNND2MB2xFipg7B1EQzF/cBSkpBIBKVVAJIBBqHZ+e0H4IcCAwFBQBhYbbQNikESgyRM7p1uHfURQbO8M0ymbo0eWsGYiYUIUQhKgBWKlzSe0U4mc19tv3ePn2Y53iJqlDWuWl/YA0kDkSwU7dYsp08XMTUqXwJuMdmUuUPvFgPYbnsN4xuaYo4ifwJqvhAo9BdX5nZm2ijLsk8x1rnIY1ISrWvseRru8PJMiXhpS5stDMl9SqlXIfFhRhW0OKqBe8ynWKniX5xm/lDykAFYAvsGo/U0+tYUYbE4uS+IUgrlK4lJ4QWJqtIDEHdmY9CXhZ4fwqsRiHmEqSD5i3NFHke5uOQIjU+J8Z5eGmE3WNAHVVCP9Ln0iTUpTqDs2FwY+lU2Dcot6w3BYqXNQJktQUk+hB3BBqCORjMSk/Z8UfMDJL6VdDY/kfWJ4IkL+9mAkF0pFCQWqoKHJiG3H11E3DS56dExNRVtx1B5dfiNo+craM6VyoyrfYnRp1xVW/BlaagEMRsQxEcUihUpTJbiJ5R4yvIBKWSJiyjZBoO5ahp0gDxOZmsIKeAngCagn/8Arp/vCUp7D3WjC27mK89zKXMRoQCkpVwv7w59+h/23PhAvg5P8v5mMBm2VGXJK1AmY4oKhIJt1PON34Lf7FJe+k/1GO3olCriS12uPmJcZneLnYibJwqOCUrSSyHLEhyV0DkFgKxdjv8AiQSkocncfcn0r+UTNPC0zz1YjDTdBWXUklSakuWUnYmrEesdx2WY5aEpTN0ndXmKH0Dx0Da4nz9VH7S5DfHEL8H58vEeZLmoCZkospt6kW2IIYiJFnhTIPsoWpStc2Y2oszAOWG5qSSTeJGm06VHdsG6LPB+eYmZiZuFxAQpUtOrUhmSQUgoJFD7XoUkV21sJvCmQIwksgcUxdZi+Z2SP4Q57uTuwbkQLHyh0wdvenr5wux893A9kfM84uzCaUhhc/SFqSS4I3buf0iStUC4JldJL5nQpi4Nd6fFnH0MTEK13535dI8KVsL7nl2/fePMprC31iOpsU7+soUE4liE7C0eyGEQkNHVLa5c/SE7y2TDtaZ7xNkqphE2W2tuJNtTWIOyh9O1U2IRjZo0TBNKRsoaRTmaA86mNs3MwvziehKFJUoDWlTA12q+zVDvt8IctQ4FoJURRlmQFBSuYQSKpSLDko8z8h1i3E4xU1XkyA6nZUyrJ5t16wmyoT56vLlqWiUzKq4Na6TdmtV27PG9yXLESkBKR6xSlBmbcxiHrACwlWR5MmUnmo3JhyhMdSI9p7RYBaSE3kAjsdJjgHxjZ6YTx/jCrFS8NNmqlSCjUpSUlTk6qkC9QE7tUxXIyfDoQTKxyEvYkaa9woH5RzxH4mlqnTJE7BpmJlrUlKlLKFULODpJD9DZoHVi8AEp1SJoF9KZr/Uj6xrdBOZXZS9uc9bzT+AcwmTZcxMxWvy16Ur/ABBqh2BLXc1ZQeHKg6ld2+AaKfDapRw8tcmWZcpQJCSADchzUuSzuSTaLJJ351+MRatwLAzp6dTs5vLhaPOIQSlQBqQQPUQPiMwlSzpWpiQ7Mo050EeTm0k/9werj6iEB0Cbr54tG7Gva0rzQ+ykJSoKUAxRqAuHuGverPaL8zmLSgKQxOoO5bh97Yk0csA8cUErKCwUNQUk3agIUPjF09LsGo/wpQxmmN6gE9VFkMpUnzEAsUlqagxHQwjzHCoWAmZLClhwHuOrioHa7wxEhcqaVI4krLrBIDVLrc1LBgEuwALNRysXhwsaktqah5jlHcDWE5xF5iMR4VU+uTNIVdl0I7KTUfD1hnmmDm/YFS1q1zAApVXNFBWkUqwDDmRDbDKJ5jveL9MRvWZmBPSUrTUDExngrMJSEzEzFpQSQQTuADY9D61gLxFj1YqeiXKBUkcKAzalH3m2Hewd7mNVj/D+GW61p8tqqUlWn1Puu+7bwDK8uSGkSwCf+5Md1V2B4iOnCOkNVlY7lBvAKkCxItHGRYMSpaJYLtc81G5+PyaCcSncOOou/Mc+28JEzJqqmYoA2YafTaAMYuYkhcqYszEVMtb/AHiaUAv8q7bAq/Ss7d7rC7dVGJrMJjgSELGhZfSD7wD260qO9xWPU8EOTa7lqd+l6xmDjxiQlaQQmjVrr1ElmqCHalabXLTL8zJGia/JKiBXorZzzYDYgG/P1uk2MSnHl5SynVuoLEQbO1hSKEEdCGu3rWND4TP/ACsrsf61Rmc6wOgKUkkJuUCocAJDOWSABYDa7UjReEFf8pK/zf1qg9Dycw634/mN3iao8Ij00dOSThVEjrRIyenLxLRDSKZ7hJNbNfmYFjaEBeAYlRUSfh2gTGZlLkjjUEkmj78yeQAqTYdI7j8UEBhfYfmeQ6wixg8srxCmKyUpTqU2nUdBSpqeS/FzO7kAxz6tEVOZYp28R0hWqgNB6/v9+toHf84Q4DHoQAFTNSUllTSQE6yaS0jcAPaiQKm8PNfK8S1FO7MetrT0VaRzMDqmsa3PeOzVUqH6QszXHolJ1LUAQH3YDmR8gBUmg5jACcCF7w3MMxTLSVrIDVZ29e3X0jEhSsdNDzFIl2Cikl2YOQT1JaA5k2ZjJlX8u7G6jspTUfkkUHzjVZfgSlLJSAGO5FSQQbdI6en0zKNxEjevTJsWjXL0eWwlzUBBNApLMnUlJFBcGrk11G2l4YyMVN1B/KKSdlEEDzAl634SfUNvCuRhiogBndTBxcqCvy+UWfZ1UZO5s34wRY8nh97G0HbTOQwjyVi5moAyVMfeCgW9pxR6hgL3UAIiMzqypU1NHco2CVK+iWbmQN4VSJagDRW+yrEn9YqVipiV1UR7Iuz+2OlKx680acNwRHkrN5StyKFVRsACbPYKHrS8epGZSlhwvncFPs3NQIRS8xmHSNRIITdjcKH7vYR7RjSW1IQrUlLugV1BiLWJA/0iNvMOmMLXlOHmYlOLC/vEgewsAEiyi1TwkC7EMC8NJmFlr9qWhQ6pSfqIQIxEtXtSkspASqpDpUAClweaUimwAsAIvwc6UFCaEqClAOyqEEgmnfboI3dFfpSOBGeYTEScOsgBKEpYBIAAfhAAsKkQBgM2lTPZVbYiBPFmYpVICAC61geg4n+IAhJ9nVK8ualylQBPQkAlJbp9OYeINSu9wB5Q0/lizCaDM8EicsL83TwhPsuKEnmOcCKyQbTh/pb/ANoLkz0TEhSVCzNyMdBjlagik+0ypDuW4jLCoCUpFDpAAPYN+Ue5q6j1/KMb4QWEYidKT7LH/wAVMPqY0mOxyJY1TFMGoLk9AN4t0bgagL6Xk2oX+WTDFqcV23ivALDakqCkqqGLjqx5O8YzNs4mTjoSClBsgXV35npb6wdl2JGDQDiJmhMx9MtipiGc0cg1AbtHXbUUg+wnM52xtu6aXGSH4033HPrFCTCaZnkubwpmoY2QFBz3Bqe0MsnxaRwKAfYt8u8TsVd7DExNUAdpEAzWeVKZCSfLoVEEpSqltipiByFb1ECYfDCqlb9eIl9+nQGym2jVY0akKTzFO9x84wPiXO/KaXLbWWKiahINv8x+ncQ96jU7Ko+YmqzM2I/UpLDhrcl7nqLQFiZsqXxzFJS6ioFRc6iK6RU22EC+F8YqbJ41alpUUksA+4LBhYtTlGewsr7XiyZhJRUt/Ak8KRyuHbrzhBq1GJu0Vkk7jxNJh88wyjpTMAJO6VIcnqoAPBeIS+0Ks18OS1IPlp0LFmJZX8JfnzgXwpjyf+XW9A6HuGuj0FR2PIQogHM2wIuJ5neISiccKU6kFkBW4UduqQ47NyEfQvCFMLLH839ao+R5inRjST/9v9TN9RH1jwrPSMMgEgF1f1qg6SqrXHUTrU2LUreREcKEUrntS5gLF5omoBIA6GrX9IDnZrLSdJUXDPwqNw4sOUMapnEYlPzh82ao3PoIkKcVnkhLalXGocKzwuQ9BzG8SFXMbtEb5TmaZmlClJ8wp1AD3k7LA/KLszm8IA3PoI+bysF5bT1TNCk1SuzHmkUJ5ci7OoUjXeHc8RiQUsUrTdKqOPxgcum3wg+1FrTOyN7iFokAEFXtW7jcHbS9nijE4JnmrOnUADLSEqKgBRLlxV6tzvBsyTzqD3c9O0VrX+IB2ID0v7vb9YSwMYJmcxw6aTgVIQgLCwkp+6QEEGUgNpOpRfUxt2iyViJkrypa0pAWNKEpJKkaUuAon2uEXDVa7vHMZiGBSP8AFJIEoVSATZQsQU3J5wpzPHScMXlhUyaoMh1KWw5JKiWS42pStmhFt3djuMxnnmbokJ1KLrNgz+jfQfQVhDl+BXiF+bPcAF0o/wDY81N8LBhEyrLJkxfmzeJZsm4H993MPUyS5CjpCbivNrjqYdTphRYcwS3VoXkuXIJUlJCbEEB+epLfBm57tBq8MxIOqnM/P1+EKRiSBQtt/b1EaPL5epAUGYgF/nF1Go37jOZqaQB7o5lUiR/lHSDsPKfoP3aL5UgC9YIhjNc4iFpec8IAAYCOkvA2Y4+VJTrmLCE2D7nkBcntCLMPGcpCdSJaljqQj9S0ASBzCasqWBNpoMTgpcxKklKeIEOAAQ+4IqCLuLR88IWH450sJJLkhZUEkkJTqSxUnYMepo52vhrPZeKQVIBSUtqSdndiDuKH4RkPEeCSMYoK1EavMSEvQqDglq+2SwBTakIrnaARKqDlx3TKMsn4laSrzbsUakJZkqFyAKAqAHNiNov+34lHCUylEE0KVIoGNyovf5dYb4fESX1LZCCCllDSFV4TxBLnSlmsGU1I5PkYdYYBISHKWKRTmG5mE9owW8clRt1iYjXjpk5KVKlhGgqDBRU9EMagMLj4xqpsgFHlqDhmIhbh5kuTLBStRSSSlN3rdy7B/wB0MCYjO5yifLlhugKj+/SI6zO4vxDv3rk3lONw03DrMyWSUbm/oofn9NpN8TK0kCWArm7gHs35x5Xm+KTUy/igj9ImCzuVqBmSUJP40pSa/B/mYlcFu8wufSMBAwDaMfB2AUnXOWCCuiXuzuT6lm7QRmWNleeZU2WhSAE8dNSX5i4TUcSTR7Q2w6gQCCCCHBG/WMznchEzELdIQ1FTdTKI0AFN2ArUnpZwSX8OqF9SWI6SbXnZRA9Y7wWCkyCooDqqXNSB+EHa/fnCTxZjsOw8yWFzAKIfY9bpH16wDmGc6QJcgUZtTejJDejt2FmFRlqJQ87FF3qJbuVHrzPS3MxadOvbGrwelpyWruV2nj+8W5dlC56tQHly39qtOiXqT1J/SNmgMAHJYM5uaXPWMvPzLETleXJSUJGyGcDZ1UCfRo4clxgGsTuK7eYtz0qGfoaQ5gTyZOw3cm01ScbNTOlqMxRlkhKk0YPwvQVD1rAMvwuETJsyYrWFaglSmfiFTS6qtQDf0C8M5qZoUiZ/iJFdtQs7bF79xGmXigtICncWOx7wivUrhlsccHr8xyOu0q/I49Zj/B6zLnqlKuoMf5kE0+GqKsjHl4zSfxKR9W+JA+MXZu0nFiYLOJlOR9oepCvjBHirCFExM9Nl78lp39QAfQxUSL56wBm5mnCIxueSfJxRWkbiYG6niHqQr4xqsrzATZYWGB94C6VbhuXKM74tWFTQAXIQAd6kk6e7H5xqoYK4MB8bYbTNRNFlMD3FQfVP9Mbzw+gfZ0U/F/UqMvn8lJlGWeQBF6jcesajw5/08vsf6jGMLWnV0ZupHtJMSGPACOL3234vjAuP8uWFHQrUFJUzKA1sAKnhtBmMdJqJbGrsatYd45nWPUhBdMtUsnSyyeXvUIv+ULZsy8CZ7ETQlXlpk6leWnWDMKQE61FIFCSXdzEhf4gnSwJavLlklAKUBc0TACTQaS+nudjEjN0208ZqonEzHLsKPVq7cob5LSZLanELUiRIW3jHtKV/F8zbJ/fwgbE+0vsIkSKOkkHMzw3VvovvfnGCyof81N6Et04jblEiRPR/dHvyJ9GyhI0GnOBJ6iJkxi3CT60r36xIkXU+BJanJi6b/ieg/pjZZH7H75RIkYPyfc9U/F9RkmPcSJFEknzT/wCUVH7XKD08s0/zK/QfCNtkWGQmSgpQlJKQ5AAeJEjTwJCPyGZ/wD/1WN/nP9aoF8bUzPDNR5YB6jWuh5xIkJreGU6Xw/cq8Wf4i/8AL/7wkxgqn+RH9AjkSI14lMa4H3O0v+hMapFh3iRIk1XEdR8U6LxnvGCBpCmDuatWw3iRIg0/5R8ymp4Y18Gf9MjufrCDxao8Vf8Aufkf1PxjkSLdD/6H+ZB/EPxL7y/wugFQcAs7UteFni7/AB1dAlulB+p+MSJD0/MfYyB/B9f4jzIEAYdLACj23e8FKiRIaeZzzyZj/C//AFcz+Rf/AOxMaxVj2iRIJ/FDq+KJfFXtyux/KH4SDl6HD/dA1rXTeOxIXq+F95bpOvtMcpZB1AkHmCxiZQHmpevEb+sSJF1PwCTt4jG2a1kqerW6RpPD3/Tyv5fziRIXV5nS0PDfE8YuYrzAHLOKOYR5rPXrUNSm1kM5s6aRIkTPOmsozdZDkEg0Dg7cokSJE6cQzP/Z")
    st.title("BANK NOTE AUNTHENTICATION")
    st.subheader("WELCOME ALL :heart:")

if selected=="Project":
    st.image("data:image/jpeg;base64,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")
    st.title("BANK NOTE AUTHENTICATION")
    with st.form("my form"):
        variance = st.text_input("Variance" )
        skewness = st.text_input("skewness" )
        curtosis = st.text_input("curtosis" )
        entropy = st.text_input("entropy")
        result=""
        submit=st.form_submit_button("predict")
        if submit:
            result=predict(variance,skewness,curtosis,entropy)
            st.success('The output is {}'.format(result))


if selected=="About Me":
    st.header("Hi, I am R.sarath kumar:wave:")
    st.subheader("A Newbie Data Scientist From Bsc Biotech Background")
    st.write("I am passionate about learning python to be more efficient and effective in **AI and ML Projects**")
    st.write("Check out my other projects in github : https://github.com/sarathkumar1304 ")

