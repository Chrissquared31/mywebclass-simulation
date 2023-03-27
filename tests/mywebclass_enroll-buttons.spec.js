// @ts-check
const { test } = require('@playwright/test')

test('Enroll-Buttons', async ({ page }) => {
  await page.goto('http://localhost:3000/')
  await page.getByRole('button', { name: 'Agree', exact: true }).click()
  await page.getByRole('link', { name: 'Enroll Now' }).first().click()
  await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('link', { name: 'Home' }).click()
  await page.getByRole('link', { name: 'Enroll Now' }).nth(1).click()
  await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('link', { name: 'Home' }).click()
  await page.getByRole('link', { name: 'Enroll Now' }).nth(2).click()
})
