import fetch from "../../conf/fetch";

export const linkAll = data => fetch('/api/queryAllLinks', data, "GET")
export const addLink = data => fetch('/api/addLink', data, 'POST')
export const deleteLink = data => fetch('/api/deleteLink', data, 'POST')
