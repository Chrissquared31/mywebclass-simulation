// @ts-check
const { test } = require('@playwright/test')

test('Courses-Button', async ({ page }) => {
  await page.goto('http://localhost:3000/')
  await page.getByRole('button', { name: 'Agree', exact: true }).click()
  await page.getByRole('link', { name: 'Courses' }).click()
})
