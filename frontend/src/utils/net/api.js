import fetch from "../../conf/fetch";

export const linkAll = data => fetch('/api/queryAllLinks', data, "GET")
