export async function safeJson(response){
  if (!response) return {}
  const contentType = response.headers && response.headers.get ? response.headers.get('content-type') : ''
  if (!contentType || !contentType.includes('application/json')){
    if (response.ok) return {}
    // try to read text for error
    const txt = await response.text().catch(()=>'')
    throw new Error(txt || `HTTP ${response.status}`)
  }
  // at this point assume JSON
  const text = await response.text()
  if (!text) {
    if (response.ok) return {}
    throw new Error(`Empty response body (status ${response.status})`)
  }
  try{
    return JSON.parse(text)
  }catch(e){
    throw new Error('Invalid JSON response')
  }
}
