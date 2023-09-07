import argparse
import logging
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from core.exceptions import LoginException

from core.sets import BAD_LOGIN, LOGFORMAT, LOGLEVEL, USER_AGENT, WSIZE

logging.basicConfig(
    level=LOGLEVEL,
    filename='noip_confirmer.log',
    filemode='a',
    format=LOGFORMAT,
)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

parser = argparse.ArgumentParser(description='NOIP auto confirmer')
parser.add_argument('username', type=str, help='NOIP service USERNAME')
parser.add_argument('password', type=str, help='NOIP service PASSWORD')
args = parser.parse_args()


def noip_confirmer():
    """
    NOIP free hosts auto confirmation script.
    No matter how mutch hosts you have.
    """
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={USER_AGENT}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"window-size={WSIZE}")

    driver = webdriver.Chrome(
        options=options)

    try:
        driver.get(url="https://noip.com/login")
        time.sleep(1)
        login_un = driver.find_element(By.NAME, 'username')
        login_un.clear()
        login_un.send_keys(args.username)
        time.sleep(1)
        login_pw = driver.find_element(By.NAME, 'password')
        login_pw.clear()
        login_pw.send_keys(args.password)
        time.sleep(1)
        driver.find_element(By.ID, 'clogs-captcha-button').click()
        logger.info('[*] Authorization check...')
        time.sleep(5)

        try:
            if driver.find_element(
                    By.XPATH,
                    f'//h1[@class="blue"'
                    f'and contains(text(), "{BAD_LOGIN}")]'):
                driver.save_screenshot('Login_failed.png')
                raise LoginException()

        except NoSuchElementException:
            pass

        logger.info('[V] Authorization complete')
        driver.get(url="https://my.noip.com/dynamic-dns")
        time.sleep(5)
        logger.info('[+] Check confirmation available')
        try:
            tr = 1
            res = 0
            while tr <= 3:
                try:
                    driver.find_element(
                        By.XPATH,
                        f'//tr[{tr}]/td[5]/button[text()="Confirm"]').click()
                    logger.info(f'    [V] Host {tr} confirmed')
                    tr += 1
                    res += 1
                    time.sleep(1)

                except NoSuchElementException:
                    tr += 1
                    time.sleep(1)
                    continue
            if res:
                logger.info(f'[V] {res} hosts was updated.')
                driver.save_screenshot('screen_result.png')
                ######
                # Set here nitification service code if you want
                # logger.info('[+] Notice')
                ######
            else:
                logger.info('[-] No hosts for confirmation')
                driver.save_screenshot('screen.png')

        except Exception as ex:
            logger.error(f'[!] Confirmation processing ERROR\n{ex}')

    except LoginException:
        logger.error('[X] Authorization failed')

    except Exception as ex:
        logger.error(f'[!] Open page or another problem\n{ex}')

    finally:
        driver.close()
        driver.quit()


def main():
    noip_confirmer()


if __name__ == '__main__':
    main()
