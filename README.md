# sdkconfig-differ
sdkconfig differ for esp-idf config files

## Install requirements
```
python3 -m pip install -r requirements.txt
```

## How to use eg
```
./sdkconfig-differ.py --conf sdkconfig --old-conf sdkconfig.old
```

## Example Output
```
CONFIG                                                      Old Value                                                   New Value
CONFIG_BT_NIMBLE_ENABLE_CONN_REATTEMPT                      ABSENT                                                      n
CONFIG_LWIP_IPV6_NUM_ADDRESSES                              ABSENT                                                      6
CONFIG_BSP_LED_RGB_GPIO                                     8                                                           48
CONFIG_IDF_TARGET                                           "esp32c6"                                                   ABSENT
``
